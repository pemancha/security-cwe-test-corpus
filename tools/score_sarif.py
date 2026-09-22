#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(value: str) -> str:
    return value.replace("\\", "/").lstrip("./")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: score_sarif.py RESULTS.sarif")
    truth = json.loads((ROOT / "ground-truth" / "catalog.json").read_text(encoding="utf-8"))["items"]
    sarif = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    observed: set[tuple[str, str]] = set()
    for run in sarif.get("runs", []):
            truth = json.loads((ROOT / "ground-truth" / "catalog.json").read_text(encoding="utf-8"))["items"]
    sarif = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    observed: set[tuple[str, str]] = set()
    for run in sarif.get("runs", []):
        rules = {str(index): rule.get("id", "") for index, rule in enumerate(run.get("tool", {}).get("driver", {}).get("rules", []))}
        for result in run.get("results", []):
            rule = result.get("ruleId") or rules.get(str(result.get("ruleIndex")), "")
            text = " ".join([rule, result.get("message", {}).get("text", "")]).upper()
            cwes = {item["cwe_id"] for item in truth if item["cwe_id"] in text}
            for location in result.get("locations", []):
                uri = normalize(location.get("physicalLocation", {}).get("artifactLocation", {}).get("uri", ""))
                for cwe in cwes:
                    observed.add((uri, cwe))

    expected = {(normalize(item["vulnerable"]["path"]), item["cwe_id"]) for item in truth}
    fixed = {(normalize(item["fixed"]["path"]), item["cwe_id"]) for item in truth}
    tp = len(expected & observed)
    fn = len(expected - observed)
    fp = len(fixed & observed)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    print(json.dumps({"true_positives":tp,"false_negatives":fn,"false_positives":fp,"precision":round(precision,4),"recall":round(recall,4),"f1":round(f1,4)}, indent=2))


if __name__ == "__main__":
    main()
