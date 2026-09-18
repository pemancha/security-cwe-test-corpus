// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-502: Deserialization of Untrusted Data
import java.io.*;
final class Fixture { static String decode(InputStream in)throws Exception{byte[] data=in.readNBytes(65536);return new String(data,java.nio.charset.StandardCharsets.UTF_8); } }
