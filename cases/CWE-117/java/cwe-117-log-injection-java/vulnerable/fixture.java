// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-117: Improper Output Neutralization for Logs
import java.util.logging.*;
final class Fixture { static void audit(String user) { Logger.getLogger("audit").info("login user=" + user); } } // VULNERABLE_SINK
