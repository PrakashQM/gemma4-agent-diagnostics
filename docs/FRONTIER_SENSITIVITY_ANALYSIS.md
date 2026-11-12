# Paper-ready subsection

## Post-hoc sensitivity analyses: solved frontier and patch-size composition

Two post-hoc analyses further illustrate why intermediate metrics and single-run gains require careful interpretation.

**Observed solved-task frontier.** On the shared 30-task cohort, four independent ALT-v1 baseline repetitions produced 30 successful runs across 120 attempts and solved 10/30 distinct issues at least once. Seven intervention batches produced 53 successful runs across 210 attempts and also solved 10/30 distinct issues at least once. The 20 issues never solved by any baseline repetition produced zero resolutions across their 140 intervention attempts. Thus, interventions changed individual run outcomes without expanding the observed set of issues solved on this frozen cohort. This is descriptive and post-hoc: it does not imply that the remaining issues are intrinsically unsolvable.

**Patch-size sensitivity.** The semantic-restraint intervention appeared to reduce median patch size from 611 to 549 characters when all runs were pooled. However, empty patches increased from 7/30 to 10/30. Restricting descriptively to non-empty outputs, the medians were 895 and 891.5 characters. Among the 18 tasks producing non-empty patches in both conditions, the median paired change was 0 characters: 8 patches shrank, 4 were unchanged, and 6 grew. The apparent unconditional improvement therefore largely reflects a change in which runs produced patches, rather than a consistent reduction in the size of comparable patches.

Together, these analyses reinforce a broader evaluation lesson: an intervention may improve an aggregate process metric or individual-run score without expanding the observed solved-task frontier or improving like-for-like outputs.


## Additional concentration and upper-bound checks

The 20 baseline-never-solved issues account for 80 baseline attempts and 140 intervention attempts, with 0 successes in 220 observed attempts on those same issues. Because attempts repeat the same issues, we report this count descriptively and do not attach an independent-trial confidence bound.

Across the initial and replication edit-recovery/control cells, only three issues change resolved status: `rich_3063`, `rich_3180`, and `rich_3278`. The other 27 issues are stable across all four cells.


## Batch-level variation and never-solved issues

Across the 11 repeated batches on the shared 30-task cohort, resolved counts are 8, 8, 6, 8, 7, 10, 7, 7, 7, 8, and 7 (mean 7.55; sample SD 1.04). Thus a one- or two-task gap between individual batches is comparable to observed batch-to-batch variation.

The 20 issues never solved in any batch remain unresolved across 220 attempts. Failure indicators are overlapping rather than mutually exclusive: 67/220 attempts have an empty patch, 46/220 encounter an agent timeout/tool/turn limit, and 197/220 have evaluator exit code 1 or 2. This shows that the never-solved frontier is not explained by a single operational failure mode.
