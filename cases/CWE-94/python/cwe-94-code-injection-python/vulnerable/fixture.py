# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-94: Improper Control of Generation of Code
def calculate(expression: str):
    return eval(expression)  # VULNERABLE_SINK
