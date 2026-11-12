# When Process Gains Fail to Improve Coding Agents

Public reproducibility resource for:

**When Process Gains Fail to Improve Coding Agents: A Replicated Intervention Study**  
Prakash Verma, 2026

> **Quick start**
>
> ```bash
> python -m pip install -r requirements.txt
> bash scripts/test_public_release_end_to_end.sh
> ```
>
> Expected final line:
>
> `PUBLIC RELEASE END-TO-END ASSERTIONS PASSED.`

[Paper PDF](paper/When_Process_Gains_Fail_to_Improve_Coding_Agents.pdf)

[Open the reproduction notebook in Colab](https://colab.research.google.com/github/prakashqm/gemma4-agent-diagnostics/blob/main/notebooks/colab/01_reproduce_paper.ipynb)

## What this repository is

This repository contains the **derived-data reproducibility package and diagnostic toolkit** for a controlled study of prompt-level process interventions in a frozen Gemma 4 31B software-engineering agent.

The central evaluation framework separates:

1. treatment assignment;
2. treatment uptake;
3. intermediate process change;
4. end-task correctness;
5. replication.

The main frozen corpus contains **416 trajectories across 91 unique issues in four repositories** (FastAPI, Rich, Requests, HTTPX). The repeatedly evaluated controlled/stress subset contains **356 trajectories across 43 unique issues in three repositories**. A separate fresh-task semantic-assistance diagnostic contributes **48 evaluation runs on 12 previously unused issues** and is not counted inside the 416-row corpus.

## Reproduce the reported analyses

Tested with **Python 3.13.5** using the pinned packages in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
bash scripts/test_public_release_end_to_end.sh
```

The end-to-end script verifies:

- manifest integrity;
- the 416-row headline assertions;
- edit-recovery and replication results;
- solved-frontier and patch-sensitivity analyses;
- 11-batch variation and never-solved failure profiles;
- fresh-task O vs O+S derived summaries;
- compliance-parser fixtures.

You can also run components separately:

```bash
python scripts/reproduce_public_analysis.py
python scripts/reproduce_frontier_sensitivity.py
python scripts/reproduce_fresh_semantic_diagnostic.py
python -m pytest -q tests/test_compliance_parser_fixtures.py
```

## Key released evidence

### Main controlled corpus

- Edit recovery: non-empty patches **42/60 → 49/60**; resolution **16/60 → 17/60**.
- Initial edit-recovery result: **10/30 vs 8/30**; independent repetition: **7/30 vs 8/30**.
- Requested semantic-falsification marker: naive serialized-trace matching **30/30**, executed-tool parsing **5/30**.
- Verification-quality audit: among 102 unresolved non-empty trajectories with an exit-zero post-edit executable check, **28** use a targeted test or explicit assertion, **70** observational probes, **2** broader tests, **2** syntax/import-only.

### Shared 30-task sensitivity

Across 11 batches, resolved counts range from **6 to 10** (mean **7.55**, sample SD **1.04**).

Task-level classification:

- **5** tasks resolve in all 11 batches;
- **20** resolve in none;
- **5** vary.

The 20 never-solved issues remain unresolved across **220 observed attempts**. Overlapping failure indicators include:

- **67/220** empty-patch attempts;
- **46/220** agent timeout/tool/turn-limit events;
- **197/220** evaluator exits 1 or 2.

These are descriptive post-hoc analyses, not independent-task inferential claims.

### Fresh-task semantic-assistance diagnostic

A separate study uses 12 previously unused evaluation issues (10 FastAPI, 2 Rich), each run twice:

- operational control (O): **4/24** resolved;
- operational + frozen semantic checklist (O+S): **2/24** resolved;
- distinct issues solved at least once: **2/12 O**, **1/12 O+S**;
- requested marked verification: **2/24 O**, **3/24 O+S**;
- same-rubric manual issue-relevant behavioral probes: **20/24 O**, **19/24 O+S**.

The four preflight runs were pre-specified harness-debugging runs and excluded before evaluation. The checklist was frozen before inference, self-reviewed, and derived only from issue statements; no reference patches, hidden tests, evaluator outputs, or candidate-run outcomes were used.

## Repository layout

```text
data/       derived trajectory-level tables and audits
docs/       methods, policy, and audit documentation
figures/    released figures
notebooks/  stripped Colab/Kaggle experiment notebooks
paper/      one canonical submission PDF + LaTeX source
scripts/    reproduction and integrity checks
tests/      synthetic compliance-parser fixtures
```

## What is intentionally not redistributed

This repository does **not** contain:

- Kaggle competition issue/problem payloads;
- repository snapshots supplied by the competition;
- Gemma model weights;
- competition wheelhouse/runtime files;
- raw controlled-study trace bundles that may contain competition-provided text;
- the private complete research archive.

Audit tables contain only task IDs, counts, boolean flags, evaluator metadata, and short categorical audit labels. Raw issue text, agent commands, code excerpts, diffs, and trace text are not included.

To rerun agent inference, use the stripped Kaggle notebooks with the official competition resources under their original terms.

## Important limitations

- One Gemma 4 31B checkpoint is studied.
- Controlled task diversity is modest.
- Several prompt-level treatments have incomplete uptake.
- The semantic-falsification comparison uses historical baseline repetitions.
- Some evaluator outcomes cannot be attributed more finely because preserved evaluator logs are incomplete.
- The 60 exploratory trajectories survive as a frozen row-level summary; their original raw trace archive was not preserved.
- Public release tables are derived measurements; claims that require raw traces are accompanied by explicit audit limitations.

## Integrity

`MANIFEST.sha256` contains SHA-256 hashes for every released file except the manifest itself.

```bash
python scripts/check_manifest.py .
```

## How to cite

See [`CITATION.cff`](CITATION.cff). The preferred citation is:

> Prakash Verma. *When Process Gains Fail to Improve Coding Agents: A Replicated Intervention Study*. 2026.

## License

Original code in this repository is released under the Apache License 2.0. Competition data, repository snapshots, model weights, and third-party resources are not redistributed and remain governed by their original terms.
