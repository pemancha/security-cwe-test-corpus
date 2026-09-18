# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-918: Server-Side Request Forgery
import urllib.request
def fetch(url: str) -> bytes:
    return urllib.request.urlopen(url).read()  # VULNERABLE_SINK
