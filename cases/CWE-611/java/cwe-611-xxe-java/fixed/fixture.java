// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-611: Improper Restriction of XML External Entity Reference
import javax.xml.parsers.*; import java.io.*;
final class Fixture { static Object parse(InputStream in)throws Exception{DocumentBuilderFactory f=DocumentBuilderFactory.newInstance();f.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);f.setFeature("http://xml.org/sax/features/external-general-entities",false);return f.newDocumentBuilder().parse(in);} }
