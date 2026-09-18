# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-209: Generation of Error Message Containing Sensitive Information
import logging
log=logging.getLogger(__name__)
def handle(operation):
    try: return operation()
    except Exception: log.exception('operation failed'); return {'error':'internal error'}
