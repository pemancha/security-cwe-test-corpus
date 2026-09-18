# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-732: Incorrect Permission Assignment for Critical Resource
import os
def protect(path: str):
    os.chmod(path,0o777)  # VULNERABLE_SINK
