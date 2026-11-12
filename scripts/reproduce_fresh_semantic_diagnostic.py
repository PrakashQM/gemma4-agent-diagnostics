#!/usr/bin/env python3
from pathlib import Path
import pandas as pd, json

ROOT=Path(__file__).resolve().parents[1]
runs=pd.read_csv(ROOT/"data/fresh_semantic_diagnostic_runs.csv")
probe=pd.read_csv(ROOT/"data/fresh_semantic_probe_audit.csv")
frontier=pd.read_csv(ROOT/"data/fresh_semantic_frontier.csv")
meta=json.loads((ROOT/"data/fresh_semantic_metadata.json").read_text())

assert len(runs)==48
assert runs["task_id"].nunique()==12

def cond(name):
    x=runs[runs.condition==name]
    return x
O=cond("O_operational")
S=cond("OS_semantic")
assert len(O)==24 and len(S)==24
assert int(O.resolved.sum())==4
assert int(S.resolved.sum())==2
assert int(O.marker_executed.sum())==2
assert int(S.marker_executed.sum())==3
assert int(O.issue_relevant_behavior_probe_observed.sum())==20
assert int(S.issue_relevant_behavior_probe_observed.sum())==19

# Issue-level frontier, repetitions kept together.
assert int(frontier.O_ever.sum())==2
assert int(frontier.OS_ever.sum())==1
assert int(frontier.O_only.sum())==1
assert int(frontier.OS_only.sum())==0

# Both run-level O-only discordances are repeated evaluations of one issue.
wide=runs.pivot_table(index=["task_id","rep"],columns="condition",values="resolved",aggfunc="first")
o_only=((wide.O_operational==True)&(wide.OS_semantic==False))
s_only=((wide.O_operational==False)&(wide.OS_semantic==True))
assert int(o_only.sum())==2
assert int(s_only.sum())==0
assert wide[o_only].reset_index().task_id.nunique()==1

assert meta["preflight_runs"]==4
assert meta["preflight_issues"]==2
assert meta["evaluation_runs"]==48

print("FRESH SEMANTIC DIAGNOSTIC ASSERTIONS PASSED.")
print("O resolved: 4/24; O+S resolved: 2/24")
print("Manual relevant probes: O 20/24; O+S 19/24")
print("Issue frontier: O 2/12; O+S 1/12; O-only 1; O+S-only 0")
