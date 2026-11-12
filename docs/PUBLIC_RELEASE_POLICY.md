# Public release policy

## Public
- paper and source
- derived trajectory-level metrics
- derived audit tables (task IDs, counts, flags, and categorical labels only)
- aggregate statistics
- analysis scripts
- experiment notebooks with outputs removed
- smoke-test notebook
- figures
- manifests
- Apache-2.0 licensed original code

## Private / not redistributed
- raw competition task payloads
- raw traces containing competition issue text or snapshot-derived content
- repository snapshots
- Kaggle model weights
- Kaggle wheelhouse
- any credentials or API tokens
- full private research archive

Audit tables contain only task IDs, counts, boolean flags, evaluator metadata, and short categorical audit labels. Raw issue text, agent commands, code excerpts, diffs, and trace text are not included.

The private archive remains the authoritative audit record for the reported experiments.
