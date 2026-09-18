# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-330: Use of Insufficiently Random Values
import secrets
def reset_token() -> str:
    return secrets.token_urlsafe(32)
