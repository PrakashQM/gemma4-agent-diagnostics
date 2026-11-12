#!/usr/bin/env python3
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
manifest=ROOT/"MANIFEST.sha256"
bad=[]
for line in manifest.read_text().splitlines():
    if not line.strip(): continue
    h,rel=line.split("  ",1)
    if rel=="MANIFEST.sha256": continue
    p=ROOT/rel
    if not p.exists(): bad.append((rel,"missing")); continue
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=h: bad.append((rel,"checksum mismatch"))
if bad:
    raise SystemExit("Manifest failures: "+repr(bad))
print("All manifest checks passed.")
