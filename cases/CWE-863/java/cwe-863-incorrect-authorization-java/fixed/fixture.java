// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-863: Incorrect Authorization
final class Fixture { static Invoice read(Store store,Actor actor,String id){Invoice invoice=store.get(id);if(!invoice.ownerId.equals(actor.id)&&!actor.admin)throw new SecurityException();return invoice;} record Invoice(String ownerId){} record Actor(String id,boolean admin){} interface Store{Invoice get(String id);} }
