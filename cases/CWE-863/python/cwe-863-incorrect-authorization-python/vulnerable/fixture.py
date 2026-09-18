# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-863: Incorrect Authorization
def read_invoice(store, invoice_id: str):
    return store.get(invoice_id)  # VULNERABLE_SINK
