# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-502: Deserialization of Untrusted Data
import json
def decode(payload: bytes):
    value=json.loads(payload.decode('utf-8'))
    if not isinstance(value,dict): raise ValueError('object required')
    return value
