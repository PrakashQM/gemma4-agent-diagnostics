# Public Release Consistency Notes

- Full corpus: 416 trajectories, 91 unique issues, 4 repositories.
- Controlled/stress subset: 356 trajectories, 43 unique issues, 3 repositories.
- Public package contains derived tables and runnable code, not raw traces or raw patches.
- Colab notebook targets this public distribution directly.
- Semantic-falsification notebook counts compliance only from executed `run_command` arguments.
- Unresolved outcomes are not automatically labeled semantic failures:
  - 236/271 unresolved controlled/stress runs have a completed nonzero evaluator exit.
  - 35/271 have verification not completed (exit -1) under an agent timeout/tool/turn limit.
- Preserved evaluator `.log` files are zero-byte; finer retrospective failure attribution is unavailable.
