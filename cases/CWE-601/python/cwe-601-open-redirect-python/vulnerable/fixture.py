# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-601: URL Redirection to Untrusted Site
def redirect(next_url: str):
    return {'status':302,'location':next_url}  # VULNERABLE_SINK
