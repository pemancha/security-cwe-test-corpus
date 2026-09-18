// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-89: Improper Neutralization of Special Elements used in an SQL Command
import java.sql.*;
final class Fixture { static ResultSet find(Connection c, String name) throws Exception { PreparedStatement p=c.prepareStatement("SELECT * FROM users WHERE name=?"); p.setString(1,name); return p.executeQuery(); } }
