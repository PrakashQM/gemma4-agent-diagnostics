# Verification Quality Annotation Rubric

This rubric refines the paper's earlier binary "exit-zero post-edit check" metric.

## Classes

### targeted_test
A pytest/unittest invocation directed at a relevant test file, test selector, or test function.
This is treated as stronger evidence because it has an explicit pass/fail oracle supplied by a test runner.

### inline_assertion
A Python verification script containing one or more explicit `assert` statements (or an equivalent
assertion failure condition) over the changed behavior.

### broad_test
A successful pytest/unittest invocation that is not clearly targeted to the changed behavior.

### observational_probe
A Python script that exercises behavior and prints/inspects output but contains no explicit assertion
or test-runner oracle. Exit code 0 only proves that the probe executed successfully.

### syntax_or_import_only
A compile/import-only check such as `py_compile`. This verifies basic executability, not behavior.

## Interpretation

For the 102 unresolved, non-empty trajectories with an exit-zero executable post-edit check:

- 28/102 (27.5%) used either a targeted test or explicit inline assertion.
- 2/102 (2.0%) used a broader test-suite check.
- 70/102 (68.6%) used observational probes without an explicit pass/fail oracle.
- 2/102 (2.0%) used syntax/import-only verification.

This means the earlier 102/162 (63.0%) metric should not be interpreted as 102 strong behavioral validations.
Most successful checks were weaker, self-authored observational probes.
