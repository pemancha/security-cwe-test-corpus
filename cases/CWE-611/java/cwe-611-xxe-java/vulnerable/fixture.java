// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-611: Improper Restriction of XML External Entity Reference
import javax.xml.parsers.*; import java.io.*;
final class Fixture { static Object parse(InputStream in)throws Exception{return DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(in);} } // VULNERABLE_SINK
