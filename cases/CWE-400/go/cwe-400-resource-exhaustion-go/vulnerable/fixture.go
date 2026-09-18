// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-400: Uncontrolled Resource Consumption
package fixture
func Allocate(count int) []byte { return make([]byte,count) } // VULNERABLE_SINK
