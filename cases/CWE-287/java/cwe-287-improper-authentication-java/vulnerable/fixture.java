// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-287: Improper Authentication
final class Fixture { static boolean authenticate(String expected,String supplied) { return supplied.startsWith(expected); } } // VULNERABLE_SINK
