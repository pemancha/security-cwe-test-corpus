# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
CONFIG={'database_password':'fixture-only-password'}
def debug_config():
    return {'database_password':'[REDACTED]'}
