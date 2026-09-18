# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-312: Cleartext Storage of Sensitive Information
import hashlib
def save_token(path, token: str):
    path.write_text(hashlib.sha256(token.encode()).hexdigest())
