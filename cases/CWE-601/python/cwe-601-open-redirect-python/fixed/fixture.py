# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-601: URL Redirection to Untrusted Site
from urllib.parse import urlparse
def redirect(next_url: str):
    parsed=urlparse(next_url)
    if parsed.scheme or parsed.netloc or not next_url.startswith('/'): raise ValueError('external redirect rejected')
    return {'status':302,'location':next_url}
