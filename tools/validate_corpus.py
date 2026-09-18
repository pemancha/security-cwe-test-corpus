#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "ground-truth" / "catalog.json"


def contained(relative: str) -> Path:
    candidate = (ROOT / relative).resolve()
    if ROOT.resolve() not in candidate.parents:
        raise AssertionError(f"path escapes repository: {relative}")
    return candidate


def main() -> None:
    document = json.loads(CATALOG.read_text(encoding="utf-8"))
    items = document["items"]
    assert document["schema_version"] == 1
    assert document["cwe_families"] == 30
    assert document["scenario_pairs"] == 60
    assert document["total_cases"] == 120
    assert len(items) == 60

    scenario_ids: set[str] = set()
    cwes: set[str] = set()
    expected_jsonl: list[str] = []

    for item in items:
        scenario_id = item["scenario_id"]
        assert scenario_id not in scenario_ids, f"duplicate scenario: {scenario_id}"
        scenario_ids.add(scenario_id)
        cwes.add(item["cwe_id"])

        vulnerable = contained(item["vulnerable"]["path"])
        fixed = contained(item["fixed"]["path"])
        assert vulnerable.is_file(), vulnerable
        assert fixed.is_file(), fixed

        vulnerable_text = vulnerable.read_text(encoding="utf-8")
        fixed_text = fixed.read_text(encoding="utf-8")
        marker_lines = [index for index, line in enumerate(vulnerable_text.splitlines(), 1) if "VULNERABLE_SINK" in line]
        assert marker_lines == item["vulnerable"]["lines"], scenario_id
        assert "VULNERABLE_SINK" not in fixed_text, scenario_id

        scenario_root = vulnerable.parent.parent
        scenario_json = json.loads((scenario_root / "expected-findings.json").read_text(encoding="utf-8"))
        assert scenario_json == item, scenario_id
        assert (scenario_root / "manifest.yaml").is_file()
        assert (scenario_root / "README.md").is_file()
        expected_jsonl.append(json.dumps(item, separators=(",", ":")))

    assert len(cwes) == 30
    actual_jsonl = [json.dumps(json.loads(line), separators=(",", ":")) for line in (ROOT / "ground-truth" / "expected-findings.jsonl").read_text(encoding="utf-8").splitlines() if line]
    assert actual_jsonl == expected_jsonl
    print(f"CORPUS_VALIDATION_OK cwes={len(cwes)} pairs={len(items)} cases={len(items) * 2}")


if __name__ == "__main__":
    main()
