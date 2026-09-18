# Security CWE Test Corpus

Controlled source-code benchmark for validating Antares, Foundry, SAST, SARIF, and AI-assisted remediation workflows.

## Scope

- **30 CWE families**
- **60 vulnerable/fixed scenario pairs**
- **120 total test cases**
- Python, JavaScript, TypeScript, Java, Go, C#, and PHP fixtures
- Machine-readable ground truth with expected file and line locations
- Safe fixed controls for false-positive measurement

The fixtures are intentionally small and deterministic. They demonstrate insecure coding patterns without exploit automation, real credentials, external targets, persistence, or deployment manifests.

## Repository layout

```text
cases/CWE-NNN/language/scenario/
├── vulnerable/fixture.ext
├── fixed/fixture.ext
├── expected-findings.json
├── manifest.yaml
└── README.md

ground-truth/
├── catalog.json
└── expected-findings.jsonl

tools/
├── validate_corpus.py
└── score_sarif.py
```

## Validation

```bash
python3 tools/validate_corpus.py
```

Expected result:

```text
CORPUS_VALIDATION_OK cwes=30 pairs=60 cases=120
```

## SARIF scoring

```bash
python3 tools/score_sarif.py scanner-results.sarif
```

The scorer compares CWE-tagged SARIF results with vulnerable cases and fixed controls, then reports true positives, false negatives, false positives, precision, recall, and F1.

## Scanner usage

Scan `cases/` or a bounded CWE/language subset. For Antares, start with `plan`, then use `query` for a specified CWE or `sweep` for repository-aware selection. See [scanner integration](docs/scanner-integration.md).

## Safety

Read [DO_NOT_DEPLOY.md](DO_NOT_DEPLOY.md) before use. Run scanners in an isolated, non-production environment. Never expose these fixtures as services.

## Publication

This repository is intended to remain private unless its owner completes legal, security, and license review.
