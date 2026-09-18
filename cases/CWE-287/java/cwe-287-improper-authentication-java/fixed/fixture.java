// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-287: Improper Authentication
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;
final class Fixture { static boolean authenticate(String expected,String supplied) { return MessageDigest.isEqual(expected.getBytes(StandardCharsets.UTF_8), supplied.getBytes(StandardCharsets.UTF_8)); } }
