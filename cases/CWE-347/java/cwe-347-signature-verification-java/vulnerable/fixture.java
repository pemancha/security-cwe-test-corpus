// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-347: Improper Verification of Cryptographic Signature
final class Fixture { static byte[] accept(byte[] document,byte[] signature){return document;} } // VULNERABLE_SINK
