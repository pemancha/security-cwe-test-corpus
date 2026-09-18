// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-347: Improper Verification of Cryptographic Signature
import java.security.Signature;
final class Fixture { static byte[] accept(Signature verifier,byte[] document,byte[] signature)throws Exception{verifier.update(document);if(!verifier.verify(signature))throw new SecurityException();return document;} }
