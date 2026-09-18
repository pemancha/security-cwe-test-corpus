# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import hashlib
def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
