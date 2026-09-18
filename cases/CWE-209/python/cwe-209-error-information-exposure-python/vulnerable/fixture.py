# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-209: Generation of Error Message Containing Sensitive Information
def handle(operation):
    try: return operation()
    except Exception as exc: return {'error':repr(exc)}  # VULNERABLE_SINK
