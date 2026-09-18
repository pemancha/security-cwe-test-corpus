# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-400: Uncontrolled Resource Consumption
MAX_ITEMS=10000
def allocate(count: int):
    if count < 0 or count > MAX_ITEMS: raise ValueError('count outside limit')
    return [0] * count
