// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-312: Cleartext Storage of Sensitive Information
import java.nio.file.*;
final class Fixture { static void save(Path p,String token)throws Exception{ Files.writeString(p,token); } } // VULNERABLE_SINK
