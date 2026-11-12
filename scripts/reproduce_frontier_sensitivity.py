#!/usr/bin/env python3
from pathlib import Path
import pandas as pd, numpy as np, matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/"data/master_trajectories_416.csv")
df["resolved_bool"] = df["resolved_bool"].astype(str).str.lower().isin(["true","1"])
df["patch_chars"] = pd.to_numeric(df["patch_chars"], errors="coerce").fillna(0)

shared = df[df["study"].isin([
    "controlled30","edit_recovery_replication","forced_localization",
    "semantic_restraint","semantic_falsification"
])].copy()

baseline_runs = [
    ("controlled30","A_alt_v1","B1"),
    ("edit_recovery_replication","A_alt_v1","B2"),
    ("forced_localization","A_alt_v1","B3"),
    ("semantic_restraint","A_alt_v1","B4"),
]
intervention_runs = [
    ("controlled30","B_verify_path","I1_verify"),
    ("controlled30","C_edit_recovery","I2_edit"),
    ("controlled30","D_graph_once","I3_graph"),
    ("edit_recovery_replication","C_edit_recovery","I4_edit_repl"),
    ("forced_localization","L_forced_localization","I5_localize"),
    ("semantic_restraint","S_semantic_restraint","I6_restraint"),
    ("semantic_falsification","F_semantic_falsification","I7_falsify"),
]

rows=[]
for study,cond,label in baseline_runs+intervention_runs:
    x=shared[(shared.study==study)&(shared.condition==cond)]
    assert len(x)==30, (study,cond,len(x))
    kind="baseline" if label.startswith("B") else "intervention"
    for _,r in x.iterrows():
        rows.append({"task_id":r.task_id,"batch":label,"kind":kind,"resolved":int(r.resolved_bool)})
heat=pd.DataFrame(rows)

base_ever=heat[heat.kind=="baseline"].groupby("task_id").resolved.max()
int_ever=heat[heat.kind=="intervention"].groupby("task_id").resolved.max()
assert int(base_ever.sum())==10
assert int(int_ever.sum())==10
never=base_ever[base_ever==0].index
assert int(int_ever.loc[never].sum())==0

frontier=pd.DataFrame([
    {"group":"Four baseline repetitions","attempts":120,"successful_runs":30,"distinct_issues_solved":10},
    {"group":"Seven intervention batches","attempts":210,"successful_runs":53,"distinct_issues_solved":10},
])
frontier.to_csv(ROOT/"data/solved_frontier_summary.csv",index=False)

pivot=heat.pivot(index="task_id",columns="batch",values="resolved").fillna(0).astype(int)
pivot["_base"]=base_ever.reindex(pivot.index).astype(int)
pivot["_int"]=int_ever.reindex(pivot.index).astype(int)
pivot=pivot.sort_values(["_base","_int"],ascending=[False,False])
cols=[x[2] for x in baseline_runs]+[x[2] for x in intervention_runs]
mat=pivot[cols].to_numpy()
fig,ax=plt.subplots(figsize=(8.2,7.2))
ax.imshow(mat,aspect="auto",interpolation="nearest")
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols,rotation=45,ha="right")
ax.set_yticks(range(len(pivot.index))); ax.set_yticklabels(pivot.index,fontsize=7)
ax.axvline(3.5,linewidth=1.2)
ax.set_xlabel("Run / intervention batch"); ax.set_ylabel("Task ID")
fig.tight_layout()
fig.savefig(ROOT/"figures/solved_frontier_heatmap.pdf",bbox_inches="tight",metadata={"CreationDate": None})
plt.close(fig)

sr=df[df.study=="semantic_restraint"]
base=sr[sr.condition=="A_alt_v1"].set_index("task_id")
rest=sr[sr.condition=="S_semantic_restraint"].set_index("task_id")
both=base.index[(base.patch_chars>0)&(rest.patch_chars>0)]
diff=rest.loc[both,"patch_chars"]-base.loc[both,"patch_chars"]

sens=pd.DataFrame([
    {"measure":"Median patch chars, all runs","baseline":base.patch_chars.median(),"restraint":rest.patch_chars.median()},
    {"measure":"Empty patches","baseline":int((base.patch_chars==0).sum()),"restraint":int((rest.patch_chars==0).sum())},
    {"measure":"Median patch chars, non-empty only","baseline":base.loc[base.patch_chars>0,"patch_chars"].median(),
     "restraint":rest.loc[rest.patch_chars>0,"patch_chars"].median()},
])
sens.to_csv(ROOT/"data/semantic_restraint_sensitivity.csv",index=False)

paired=pd.DataFrame({
    "task_id":both,
    "baseline_patch_chars":base.loc[both,"patch_chars"].values,
    "restraint_patch_chars":rest.loc[both,"patch_chars"].values,
    "paired_change_restraint_minus_baseline":diff.values,
})
paired.to_csv(ROOT/"data/semantic_restraint_paired_nonempty.csv",index=False)

assert len(both)==18
assert float(diff.median())==0.0
assert int((diff<0).sum())==8
assert int((diff==0).sum())==4
assert int((diff>0).sum())==6


# Additional post-hoc checks used in the competition paper.
assert len(never)==20
assert 20*4 + 20*7 == 220

er = df[df.study.isin(["controlled30","edit_recovery_replication"]) & df.condition.isin(["A_alt_v1","C_edit_recovery"])]
er_pivot = er.pivot_table(index="task_id", columns=["study","condition"], values="resolved_bool", aggfunc="first")
varying = er_pivot[er_pivot.nunique(axis=1)>1].index.tolist()
assert set(varying) == {"rich_3063","rich_3180","rich_3278"}
assert len(er_pivot) - len(varying) == 27
print("Baseline-never-solved subset: 0/220 observed attempts (descriptive; repeated tasks)")
print("Edit-recovery status changes are confined to:", ", ".join(sorted(varying)))


# 5/20/5 frontier classification across all eleven shared-cohort batches.
counts = heat.groupby("task_id")["resolved"].sum()
always = int((counts == 11).sum())
never = int((counts == 0).sum())
variable = int(((counts > 0) & (counts < 11)).sum())
assert (always, never, variable) == (5, 20, 5)
print(f"11-batch frontier: always/never/variable = {always}/{never}/{variable}")

# Batch-to-batch variation and never-solved failure profile.
batch_counts = heat.groupby("batch")["resolved"].sum().reindex(cols)
assert batch_counts.tolist() == [8,8,6,8,7,10,7,7,7,8,7]
assert abs(float(batch_counts.mean()) - 7.545454545454546) < 1e-12
assert abs(float(batch_counts.std(ddof=1)) - 1.0357254813546264) < 1e-12

never_ids = counts[counts == 0].index
never_runs = shared[shared.task_id.isin(never_ids)].copy()
never_runs["empty_patch"] = never_runs["patch_chars"].eq(0)
never_runs["agent_limit"] = never_runs["error"].fillna("").str.contains(
    "timeout|tool call budget|turn limit|turn budget|turns budget|session timeout", case=False, regex=True
)
never_runs["eval_exit_1_or_2"] = pd.to_numeric(never_runs["test_exit_code"], errors="coerce").isin([1,2])
assert len(never_runs) == 220
assert int(never_runs.empty_patch.sum()) == 67
assert int(never_runs.agent_limit.sum()) == 46
assert int(never_runs.eval_exit_1_or_2.sum()) == 197
print(f"Batch resolved counts: {batch_counts.tolist()} | mean={batch_counts.mean():.2f}, sample SD={batch_counts.std(ddof=1):.2f}")
print("Never-solved 20 issues across 220 attempts: empty patch=67, agent limit=46, evaluator exit 1/2=197 (overlapping categories)")

print("FRONTIER/SENSITIVITY ASSERTIONS PASSED.")
print(frontier.to_string(index=False))
print()
print(sens.to_string(index=False))
print(f"Paired non-empty: n={len(both)}, median delta={diff.median():.1f}, shrink/same/grow={(diff<0).sum()}/{(diff==0).sum()}/{(diff>0).sum()}")
