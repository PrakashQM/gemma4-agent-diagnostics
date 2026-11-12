# Full trajectory reruns on Kaggle

The included experiment notebooks were the notebooks used for the controlled studies. They expect the official Kaggle competition runtime and attached inputs.

## Required external inputs
These are intentionally **not** redistributed in this package:
1. Gemma 4 Developer Agent competition dataset / issue snapshots.
2. Gemma 4 31B model version used by the competition.
3. The competition wheelhouse / `swegemma` runtime dependencies.

Join the Kaggle competition and attach the current official versions.

## Preserved run notebooks

Start with `alt_v1_two_task_smoke_test.ipynb` to confirm the runtime, model server, and tool execution work on two tasks.

Recommended order for the controlled studies:
1. `controlled30_four_conditions.ipynb`
2. `edit_recovery_replication30.ipynb`
3. `requests_verification_path_13x2.ipynb`
4. `forced_localization_30x2.ipynb`
5. `semantic_restraint_30x2.ipynb`
6. `semantic_falsification_30.ipynb`

The fresh-task semantic-assistance diagnostic is `operational_vs_semantic_12x2x2.ipynb`.

The exploratory diagnostic notebook (`exploratory_random60_diagnostics.ipynb`) is also included, but its original raw trace archive was not preserved.

## Model/runtime configuration used

- Model: `gemma-4-31b-it-qat-w4a16-ct`
- `max_tool_calls`: 28
- `max_turns`: 80
- `max_time_minutes`: 8
- temperature: 0.2
- thinking budget: 4096
- single agent
- tools: `run_command`, `read_file`, `edit_file`, `write_file`, `get_status`, `submit_patch`, `get_code_neighbors`, `search_similar_code`, `get_code_subgraph`

The exact agent YAML, sampling YAML, evaluation config, and system prompt are embedded in each experiment notebook (`ORIGINAL_ALT_V1_B64`) and are written into each run's output ZIP.

## Kaggle API

The paper-analysis reproduction does **not** need a Kaggle API token.

A Kaggle API token is only useful if you want Colab to download public competition resources for which your Kaggle account already has permission. Competition rules/acceptance may still require browser-side acceptance. Never commit `kaggle.json` to a public repository.

## Validation after rerun

Each notebook emits its own research/checkpoint ZIP. Compare the outputs statistically with `EXPECTED_RESULTS.json`. Stochastic agent trajectories are not expected to reproduce bit-for-bit; the preserved raw bundles are the authoritative record for the paper.
