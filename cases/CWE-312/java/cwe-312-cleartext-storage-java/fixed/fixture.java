// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-312: Cleartext Storage of Sensitive Information
import java.nio.file.*; import java.security.*; import java.util.*;
final class Fixture { static void save(Path p,String token)throws Exception{ byte[] d=MessageDigest.getInstance("SHA-256").digest(token.getBytes()); Files.writeString(p,Base64.getEncoder().encodeToString(d)); } }
