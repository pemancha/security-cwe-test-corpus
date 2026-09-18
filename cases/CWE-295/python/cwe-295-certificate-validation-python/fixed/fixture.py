# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-295: Improper Certificate Validation
import ssl
def context():
    return ssl.create_default_context()
