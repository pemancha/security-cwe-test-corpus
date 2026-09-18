// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-400: Uncontrolled Resource Consumption
package fixture
import "errors"
func Allocate(count int)([]byte,error){if count<0||count>1048576{return nil,errors.New("outside limit")};return make([]byte,count),nil}
