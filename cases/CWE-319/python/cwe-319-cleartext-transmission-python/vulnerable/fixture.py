# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-319: Cleartext Transmission of Sensitive Information
import urllib.request
def send(secret: str):
    return urllib.request.urlopen('http://service.invalid/?token='+secret).status  # VULNERABLE_SINK
