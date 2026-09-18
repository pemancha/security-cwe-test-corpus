# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import hashlib
def digest(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()  # VULNERABLE_SINK
