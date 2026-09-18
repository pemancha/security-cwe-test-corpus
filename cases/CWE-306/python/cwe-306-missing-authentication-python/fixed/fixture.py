# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-306: Missing Authentication for Critical Function
def delete_account(actor: dict, user_id: str):
    if not actor.get('authenticated') or actor.get('id') != user_id: raise PermissionError('forbidden')
    return {'deleted':user_id}
