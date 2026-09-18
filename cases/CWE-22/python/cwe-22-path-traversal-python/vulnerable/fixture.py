# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-22: Improper Limitation of a Pathname to a Restricted Directory
from pathlib import Path

def read_file(name: str) -> str:
    return (Path('/srv/data') / name).read_text()  # VULNERABLE_SINK
