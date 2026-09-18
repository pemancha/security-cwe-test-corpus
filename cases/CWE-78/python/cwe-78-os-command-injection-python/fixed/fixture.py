# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-78: Improper Neutralization of Special Elements used in an OS Command
import subprocess

def lookup(host: str) -> str:
    return subprocess.check_output(['nslookup', host], shell=False, text=True)
