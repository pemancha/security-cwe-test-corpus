# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-502: Deserialization of Untrusted Data
import pickle
def decode(payload: bytes):
    return pickle.loads(payload)  # VULNERABLE_SINK
