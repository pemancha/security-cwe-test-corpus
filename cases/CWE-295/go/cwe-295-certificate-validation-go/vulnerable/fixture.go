// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-295: Improper Certificate Validation
package fixture
import "crypto/tls"
func Config() *tls.Config { return &tls.Config{InsecureSkipVerify:true} } // VULNERABLE_SINK
