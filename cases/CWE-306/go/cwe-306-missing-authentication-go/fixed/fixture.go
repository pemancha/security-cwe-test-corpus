// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-306: Missing Authentication for Critical Function
package fixture
import "errors"
func DeleteAccount(actorID,userID string,authenticated bool)(string,error){ if !authenticated || actorID!=userID{return "",errors.New("forbidden")}; return userID,nil }
