# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-330: Use of Insufficiently Random Values
import random
def reset_token() -> str:
    return str(random.random())  # VULNERABLE_SINK
