# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-312: Cleartext Storage of Sensitive Information
def save_token(path, token: str):
    path.write_text(token)  # VULNERABLE_SINK
