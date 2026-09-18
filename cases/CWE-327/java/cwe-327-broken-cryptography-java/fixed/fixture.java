// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import java.security.*;
final class Fixture { static byte[] digest(byte[] data)throws Exception{return MessageDigest.getInstance("SHA-256").digest(data);} }
