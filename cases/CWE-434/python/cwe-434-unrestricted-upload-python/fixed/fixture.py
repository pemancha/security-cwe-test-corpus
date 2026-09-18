# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-434: Unrestricted Upload of File with Dangerous Type
ALLOWED={'.txt','.json'}
def save_upload(root, upload):
    suffix=upload.filename.rsplit('.',1)[-1].lower()
    if '.'+suffix not in ALLOWED: raise ValueError('type rejected')
    target=root / ('upload.'+suffix)
    target.write_bytes(upload.data)
    return target
