# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-295: Improper Certificate Validation
import ssl
def context():
    return ssl._create_unverified_context()  # VULNERABLE_SINK
