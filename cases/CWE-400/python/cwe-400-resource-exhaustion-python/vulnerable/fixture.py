# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-400: Uncontrolled Resource Consumption
def allocate(count: int):
    return [0] * count  # VULNERABLE_SINK
