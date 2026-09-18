# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-863: Incorrect Authorization
def read_invoice(store, actor: dict, invoice_id: str):
    invoice=store.get(invoice_id)
    if invoice.owner_id != actor.get('id') and 'billing-admin' not in actor.get('roles',[]): raise PermissionError('forbidden')
    return invoice
