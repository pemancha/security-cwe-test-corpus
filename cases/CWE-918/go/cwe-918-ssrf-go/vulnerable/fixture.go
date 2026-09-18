// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-918: Server-Side Request Forgery
package fixture
import ("io";"net/http")
func Fetch(url string)([]byte,error){r,e:=http.Get(url);if e!=nil{return nil,e};defer r.Body.Close();return io.ReadAll(r.Body)} // VULNERABLE_SINK
