// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-209: Generation of Error Message Containing Sensitive Information
final class Fixture { static String handle(Exception error) { return error.toString(); } } // VULNERABLE_SINK
