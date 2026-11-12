from pathlib import Path
import json
import pytest

MARKER = "SEMANTIC_FALSIFICATION_CHECK"
FIXTURE_DIR = Path(__file__).resolve().parent / "parser_fixtures"

def executed_marker(trace):
    for step in trace.get("steps", []):
        if step.get("source") != "agent":
            continue
        for call in step.get("tool_calls") or []:
            if call.get("function_name") != "run_command":
                continue
            args = call.get("arguments") or {}
            if MARKER in str(args.get("command", "")):
                return True
    return False

@pytest.mark.parametrize("fixture_path", sorted(FIXTURE_DIR.glob("*.json")), ids=lambda p: p.name)
def test_marker_execution_fixture(fixture_path):
    data = json.loads(fixture_path.read_text())
    assert executed_marker(data) == bool(data["expected_marker_execution"])

if __name__ == "__main__":
    for p in sorted(FIXTURE_DIR.glob("*.json")):
        d = json.loads(p.read_text())
        got = executed_marker(d)
        exp = bool(d["expected_marker_execution"])
        assert got == exp, f"{p.name}: expected {exp}, got {got}"
        print(f"PASS {p.name}: {got}")
    print("PARSER FIXTURE ASSERTIONS PASSED.")
