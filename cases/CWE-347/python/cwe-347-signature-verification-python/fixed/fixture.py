# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-347: Improper Verification of Cryptographic Signature
def accept_document(verifier, document: bytes, signature: bytes) -> bytes:
    verifier.verify(signature,document)
    return document
