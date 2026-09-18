# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-22: Improper Limitation of a Pathname to a Restricted Directory
from pathlib import Path

BASE = Path('/srv/data').resolve()

def read_file(name: str) -> str:
    candidate = (BASE / name).resolve()
    if BASE not in candidate.parents:
        raise ValueError('path outside repository')
    return candidate.read_text()
