# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-89: Improper Neutralization of Special Elements used in an SQL Command
def find_user(connection, username: str):
    return connection.execute('SELECT * FROM users WHERE name = ?', (username,)).fetchone()
