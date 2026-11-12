# Fresh-task semantic-assistance diagnostic

This secondary study is separate from the frozen 416-trajectory main corpus.

## Design
- 12 previously unused evaluation issues: 10 FastAPI, 2 Rich.
- Two repetitions per condition: 48 evaluation runs total.
- Two pre-specified preflight issues (one FastAPI, one Rich), run once in each condition: 4 preflight runs.
- Preflight runs were used only to debug the harness and were excluded before evaluation began.
- O (operational control): edit recovery, workspace-import verification, generic behavioral-review guidance.
- O+S: identical operational support plus a frozen, self-reviewed behavioral checklist.
- Checklist source: issue statements only, frozen before inference. No reference patches, hidden tests, evaluator outputs, or candidate-run outcomes were used.

## Results
- Resolution: O 4/24; O+S 2/24.
- The two run-level O-only discordances are both repetitions of `rich_3777`; therefore there is one discordant issue at issue level.
- Distinct issues solved at least once: O 2/12; O+S 1/12; O-only frontier 1; O+S-only frontier 0.
- Requested marked verification executed: O 2/24; O+S 3/24.
- Same-rubric manual issue-relevant behavioral probe: O 20/24; O+S 19/24.

## Interpretation
The checklist did not produce an observed increase in generic behavioral checking or task resolution in this small fresh-task study. Low explicit marker uptake means the experiment should not be interpreted as a clean efficacy test of semantic assistance.

Run:

`python scripts/reproduce_fresh_semantic_diagnostic.py`

Expected:

`FRESH SEMANTIC DIAGNOSTIC ASSERTIONS PASSED.`
