# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-78: Improper Neutralization of Special Elements used in an OS Command
import subprocess

def lookup(host: str) -> str:
    return subprocess.check_output('nslookup ' + host, shell=True, text=True)  # VULNERABLE_SINK
