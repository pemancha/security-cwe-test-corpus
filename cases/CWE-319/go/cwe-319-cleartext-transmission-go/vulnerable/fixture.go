// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-319: Cleartext Transmission of Sensitive Information
package fixture
import "net/http"
func Send(secret string)(*http.Response,error){return http.Get("http://service.invalid/?token="+secret)} // VULNERABLE_SINK
