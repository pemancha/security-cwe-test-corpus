// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-117: Improper Output Neutralization for Logs
import java.util.logging.*;
final class Fixture { static void audit(String user) { String clean=user.replace('\r','_').replace('\n','_'); Logger.getLogger("audit").info("login user=" + clean); } }
