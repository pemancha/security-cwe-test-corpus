// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-209: Generation of Error Message Containing Sensitive Information
final class Fixture { static String handle(Exception error) { System.err.println("request failed: "+error.getClass().getSimpleName()); return "internal error"; } }
