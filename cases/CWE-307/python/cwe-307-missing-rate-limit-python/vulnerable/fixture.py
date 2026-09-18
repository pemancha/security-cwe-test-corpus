# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-307: Improper Restriction of Excessive Authentication Attempts
def login(store, username: str, password: str) -> bool:
    return store.verify(username,password)  # VULNERABLE_SINK
