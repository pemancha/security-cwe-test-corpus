// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-611: Improper Restriction of XML External Entity Reference
using System.IO; using System.Xml;
public static class Fixture { public static XmlDocument Parse(string xml){var settings=new XmlReaderSettings{DtdProcessing=DtdProcessing.Prohibit,XmlResolver=null};using var reader=XmlReader.Create(new StringReader(xml),settings);var doc=new XmlDocument{XmlResolver=null};doc.Load(reader);return doc;} }
