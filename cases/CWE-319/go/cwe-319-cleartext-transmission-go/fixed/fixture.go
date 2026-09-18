// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-319: Cleartext Transmission of Sensitive Information
package fixture
import ("net/http";"net/url";"strings")
func Send(secret string)(*http.Response,error){return http.Post("https://service.invalid/session","application/x-www-form-urlencoded",strings.NewReader(url.Values{"token":{secret}}.Encode()))}
