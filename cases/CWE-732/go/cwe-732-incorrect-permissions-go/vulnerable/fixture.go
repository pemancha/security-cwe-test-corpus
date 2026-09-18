// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-732: Incorrect Permission Assignment for Critical Resource
package fixture
import "os"
func Protect(path string) error{return os.Chmod(path,0777)} // VULNERABLE_SINK
