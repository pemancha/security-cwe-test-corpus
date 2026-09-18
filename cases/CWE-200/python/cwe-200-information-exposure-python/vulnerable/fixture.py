# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
CONFIG={'database_password':'fixture-only-password'}
def debug_config():
    return CONFIG  # VULNERABLE_SINK
