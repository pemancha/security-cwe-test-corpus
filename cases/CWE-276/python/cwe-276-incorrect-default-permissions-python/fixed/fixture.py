# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-276: Incorrect Default Permissions
import os
def create(path: str):
    fd=os.open(path, os.O_CREAT|os.O_EXCL|os.O_WRONLY, 0o600)
    os.close(fd)
