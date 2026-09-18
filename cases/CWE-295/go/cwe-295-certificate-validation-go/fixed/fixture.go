// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-295: Improper Certificate Validation
package fixture
import "crypto/tls"
func Config() *tls.Config { return &tls.Config{MinVersion:tls.VersionTLS12} }
