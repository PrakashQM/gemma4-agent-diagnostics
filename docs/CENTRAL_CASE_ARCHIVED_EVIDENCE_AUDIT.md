# Central-case archived evidence audit

This audit covers the ten edit-recovery rescue cases using the preserved patch, trace, original evaluator result, and agent-limit metadata. It does **not** claim a fresh re-evaluation: the public/private archives preserve patches and traces but not the official repository snapshots/wheelhouse needed to rerun the evaluator locally.

A fresh patch re-evaluation should therefore be run only in the official Kaggle environment and labeled as a re-evaluation of archived patches; original outcomes must remain unchanged.

| Study | Task | Original outcome | Eval exit | Archived interpretation |
|---|---|---:|---:|---|
| initial | `fastapi_13207` | unresolved | 2 | Semantic fix remains incorrect |
| initial | `fastapi_14262` | unresolved | 2 | Incomplete implementation |
| initial | `fastapi_15280` | unresolved | 1 | Overbroad/speculative implementation |
| initial | `rich_3063` | resolved | 0 | Resolved |
| initial | `rich_3278` | resolved | 0 | Resolved |
| initial | `rich_3938` | unresolved | 1 | Plausible but semantically insufficient |
| initial | `rich_3942` | unresolved | 1 | Regression / failed invariant |
| replication | `fastapi_14262` | unresolved | 2 | Incomplete implementation |
| replication | `rich_3180` | unresolved | 1 | Weak/confirmatory verification of wrong hypothesis |
| replication | `rich_3942` | unresolved | 1 | Specification misinterpretation / unsupported guess |
