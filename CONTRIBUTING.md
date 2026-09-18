# Contributing

Every new scenario must include:

1. One vulnerable source fixture containing exactly one `VULNERABLE_SINK` marker.
2. A matched fixed source fixture without that marker.
3. `manifest.yaml` and `expected-findings.json`.
4. A CWE identifier, language, category, expected path, and exact vulnerable line.
5. No real secret, exploit automation, external target, deployment manifest, or required network access.

Run `python3 tools/validate_corpus.py` before review. Changes to ground truth require security-reviewer approval.
