# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-287: Improper Authentication
import hmac
def authenticate(expected: str, supplied: str) -> bool:
    return hmac.compare_digest(expected, supplied)
