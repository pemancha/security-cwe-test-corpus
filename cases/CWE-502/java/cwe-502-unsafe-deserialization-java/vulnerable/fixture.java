// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-502: Deserialization of Untrusted Data
import java.io.*;
final class Fixture { static Object decode(InputStream in)throws Exception{return new ObjectInputStream(in).readObject();} } // VULNERABLE_SINK
