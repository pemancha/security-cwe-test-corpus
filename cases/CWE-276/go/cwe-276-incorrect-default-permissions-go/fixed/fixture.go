// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-276: Incorrect Default Permissions
package fixture
import "os"
func Create(path string) error { return os.WriteFile(path, []byte("data"), 0600) }
