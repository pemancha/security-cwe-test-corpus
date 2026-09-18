# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-306: Missing Authentication for Critical Function
def delete_account(user_id: str):
    return {'deleted':user_id}  # VULNERABLE_SINK
