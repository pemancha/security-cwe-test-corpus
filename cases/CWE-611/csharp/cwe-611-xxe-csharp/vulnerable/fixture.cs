// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-611: Improper Restriction of XML External Entity Reference
using System.Xml;
public static class Fixture { public static XmlDocument Parse(string xml){var doc=new XmlDocument();doc.XmlResolver=new XmlUrlResolver();doc.LoadXml(xml);return doc;} } // VULNERABLE_SINK
