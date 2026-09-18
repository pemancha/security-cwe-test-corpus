# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-918: Server-Side Request Forgery
import ipaddress, socket, urllib.parse, urllib.request
def fetch(url: str) -> bytes:
    parsed=urllib.parse.urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname: raise ValueError('https required')
    addresses=socket.getaddrinfo(parsed.hostname,443,type=socket.SOCK_STREAM)
    if any(ipaddress.ip_address(item[4][0]).is_private for item in addresses): raise ValueError('private address rejected')
    return urllib.request.urlopen(url,timeout=3).read(1048576)
