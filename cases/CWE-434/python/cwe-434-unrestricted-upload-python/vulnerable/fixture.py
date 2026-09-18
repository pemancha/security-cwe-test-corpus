# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-434: Unrestricted Upload of File with Dangerous Type
def save_upload(root, upload):
    target=root / upload.filename
    target.write_bytes(upload.data)  # VULNERABLE_SINK
    return target
