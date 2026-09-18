// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import java.security.*;
final class Fixture { static byte[] digest(byte[] data)throws Exception{return MessageDigest.getInstance("MD5").digest(data);} } // VULNERABLE_SINK
