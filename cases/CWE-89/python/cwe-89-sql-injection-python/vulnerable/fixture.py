# CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
# CWE-89: Improper Neutralization of Special Elements used in an SQL Command
def find_user(connection, username: str):
    return connection.execute("SELECT * FROM users WHERE name='" + username + "'").fetchone()  # VULNERABLE_SINK
