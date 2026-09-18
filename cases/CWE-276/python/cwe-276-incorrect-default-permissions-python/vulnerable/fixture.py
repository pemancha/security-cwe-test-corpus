# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-276: Incorrect Default Permissions
import os
def create(path: str):
    fd=os.open(path, os.O_CREAT|os.O_WRONLY, 0o666)  # VULNERABLE_SINK
    os.close(fd)
