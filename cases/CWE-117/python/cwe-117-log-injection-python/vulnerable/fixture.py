# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-117: Improper Output Neutralization for Logs
import logging
log=logging.getLogger(__name__)
def audit(username: str):
    log.info('login user=%s', username)  # VULNERABLE_SINK
