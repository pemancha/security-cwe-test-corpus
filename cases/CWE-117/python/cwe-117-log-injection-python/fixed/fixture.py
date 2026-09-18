# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-117: Improper Output Neutralization for Logs
import logging
log=logging.getLogger(__name__)
def audit(username: str):
    clean=username.replace('\r','_').replace('\n','_')
    log.info('login user=%s', clean)
