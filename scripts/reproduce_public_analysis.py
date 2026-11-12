#!/usr/bin/env python3
from pathlib import Path
import json, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data/master_trajectories_416.csv"
EXPECTED = json.loads((ROOT / "EXPECTED_RESULTS.json").read_text())

df = pd.read_csv(MASTER)
assert len(df) == EXPECTED["trajectory_rows"], (len(df), EXPECTED["trajectory_rows"])

print("=== Public frozen corpus ===")
print("rows:", len(df))
if {"study","condition"}.issubset(df.columns):
    print(df.groupby(["study","condition"]).size().to_string())

# The public package intentionally omits raw competition traces and task payloads.
# We verify the paper's published derived tables directly.
def b(s):
    return s.astype(str).str.lower().isin(["true","1"])

if "resolved_bool" in df:
    df["resolved_bool"] = b(df["resolved_bool"])
if "patch_chars" in df:
    df["patch_chars"] = pd.to_numeric(df["patch_chars"], errors="coerce").fillna(0)

er = df[df.study.isin(["controlled30","edit_recovery_replication"]) &
        df.condition.isin(["A_alt_v1","C_edit_recovery"])].copy()
base = er[er.condition=="A_alt_v1"]
cand = er[er.condition=="C_edit_recovery"]
assert int((base.patch_chars>0).sum()) == 42
assert int((cand.patch_chars>0).sum()) == 49
assert int(base.resolved_bool.sum()) == 16
assert int(cand.resolved_bool.sum()) == 17

rq = df[df.study=="requests_verification"]
assert int(rq[rq.condition=="A_alt_v1"].resolved_bool.sum()) == 1
assert int(rq[rq.condition=="B_verify_path"].resolved_bool.sum()) == 1

fl = df[df.study=="forced_localization"]
assert int(fl[fl.condition=="A_alt_v1"].resolved_bool.sum()) == 6
assert int(fl[fl.condition=="L_forced_localization"].resolved_bool.sum()) == 7

sr = df[df.study=="semantic_restraint"]
assert int(sr[sr.condition=="A_alt_v1"].resolved_bool.sum()) == 8
assert int(sr[sr.condition=="S_semantic_restraint"].resolved_bool.sum()) == 8
assert float(sr[sr.condition=="A_alt_v1"].patch_chars.median()) == 611.0
assert float(sr[sr.condition=="S_semantic_restraint"].patch_chars.median()) == 549.0

sf = df[df.study=="semantic_falsification"]
assert int(sf.resolved_bool.sum()) == 7

print()
print("PUBLIC RELEASE HEADLINE ASSERTIONS PASSED.")
print("Note: raw competition traces are intentionally excluded; full reruns use official Kaggle inputs.")
