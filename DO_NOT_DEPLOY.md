# Do not deploy

This repository deliberately contains vulnerable source-code patterns for defensive scanner evaluation.

- Do not deploy, host, expose, package, or run the vulnerable fixtures as network services.
- Do not copy fixture credentials or insecure configurations into another application.
- Do not attach production data, credentials, endpoints, or infrastructure.
- Do not use the corpus to generate exploit payloads or target systems.
- Run analysis with network access disabled wherever practical.
- Destroy temporary workspaces after evaluation.

The fixtures are static test inputs. The repository-wide validator reads files and metadata but does not execute vulnerable code.
