// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-89: Improper Neutralization of Special Elements used in an SQL Command
import java.sql.*;
final class Fixture { static ResultSet find(Connection c, String name) throws Exception { return c.createStatement().executeQuery("SELECT * FROM users WHERE name='" + name + "'"); } } // VULNERABLE_SINK
