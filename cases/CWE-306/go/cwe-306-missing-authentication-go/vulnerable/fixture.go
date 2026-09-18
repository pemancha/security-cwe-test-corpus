// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-306: Missing Authentication for Critical Function
package fixture
func DeleteAccount(userID string) string { return userID } // VULNERABLE_SINK
