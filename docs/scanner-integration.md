# Scanner integration

## Antares

Upload the repository as a ZIP, import it through the approved Git path, or place it in the controlled OpenShift repository workspace.

- Use Plan to inspect automatic CWE selection.
- Use Query with one explicit CWE for deterministic tests.
- Use Sweep with Adaptive Auto for repository-driven coverage.
- Score the generated JSON or SARIF against `ground-truth/`.

Antares performs file-level localization. Line-level comparison applies to the separate code-review/advisor stage.

## Foundry

Register the repository as a dedicated benchmark target. Run each supported scanner through the normal isolated workflow and retain the workflow ID, commit SHA, scanner version, ruleset version, runtime isolation evidence, report artifact, and persistence/API/UI evidence.

## Recommended execution controls

- Read-only source mount.
- Network disabled unless the scanner requires an approved internal endpoint.
- Two CPU and four GiB memory starting limit per scanner job.
- Ten-second command timeout for fixture inspection tools where supported.
- No production credentials or service accounts.
- Ephemeral workspace destroyed after the result is persisted.
