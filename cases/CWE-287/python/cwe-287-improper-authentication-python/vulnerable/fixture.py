# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-287: Improper Authentication
def authenticate(expected: str, supplied: str) -> bool:
    return supplied.startswith(expected)  # VULNERABLE_SINK
