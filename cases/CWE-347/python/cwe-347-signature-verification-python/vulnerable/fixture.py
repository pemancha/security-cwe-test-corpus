# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-347: Improper Verification of Cryptographic Signature
def accept_document(document: bytes, signature: bytes) -> bytes:
    return document  # VULNERABLE_SINK
