// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-918: Server-Side Request Forgery
package fixture
import ("errors";"io";"net";"net/http";"net/url")
func Fetch(raw string)([]byte,error){u,e:=url.Parse(raw);if e!=nil||u.Scheme!="https"{return nil,errors.New("https required")};ips,e:=net.LookupIP(u.Hostname());if e!=nil{return nil,e};for _,ip:=range ips{if ip.IsPrivate()||ip.IsLoopback(){return nil,errors.New("private address rejected")}};client:=http.Client{};r,e:=client.Get(u.String());if e!=nil{return nil,e};defer r.Body.Close();return io.ReadAll(io.LimitReader(r.Body,1048576))}
