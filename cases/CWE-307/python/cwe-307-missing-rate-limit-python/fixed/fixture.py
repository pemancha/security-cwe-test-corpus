# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-307: Improper Restriction of Excessive Authentication Attempts
def login(store, limiter, username: str, password: str) -> bool:
    if not limiter.allow(username): raise RuntimeError('rate limited')
    return store.verify(username,password)
