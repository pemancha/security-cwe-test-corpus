# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-319: Cleartext Transmission of Sensitive Information
import urllib.parse, urllib.request
def send(secret: str):
    request=urllib.request.Request('https://service.invalid/session', data=urllib.parse.urlencode({'token':secret}).encode(), method='POST')
    return urllib.request.urlopen(request).status
