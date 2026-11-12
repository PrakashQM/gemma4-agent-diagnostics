#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python scripts/check_manifest.py .
python scripts/reproduce_public_analysis.py
python scripts/reproduce_frontier_sensitivity.py
python scripts/reproduce_fresh_semantic_diagnostic.py
python -m pytest -q tests/test_compliance_parser_fixtures.py

printf '%s\n' 'PUBLIC RELEASE END-TO-END ASSERTIONS PASSED.'
