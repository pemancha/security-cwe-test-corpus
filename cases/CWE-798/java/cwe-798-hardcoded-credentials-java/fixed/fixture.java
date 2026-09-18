// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-798: Use of Hard-coded Credentials
final class Fixture { static final String USER=System.getenv("SERVICE_USERNAME"); static final String PASSWORD=System.getenv("SERVICE_PASSWORD"); }
