# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-732: Incorrect Permission Assignment for Critical Resource
import os
def protect(path: str):
    os.chmod(path,0o600)
