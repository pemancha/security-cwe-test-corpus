// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-863: Incorrect Authorization
final class Fixture { static Object read(Store store,String invoiceId){return store.get(invoiceId);} interface Store{Object get(String id);} } // VULNERABLE_SINK
