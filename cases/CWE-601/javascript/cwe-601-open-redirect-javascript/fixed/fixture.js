// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-601: URL Redirection to Untrusted Site
export function redirect(next){const parsed=new URL(next,'https://application.invalid');if(parsed.origin!=='https://application.invalid')throw new Error('external redirect rejected');return {status:302,headers:{location:parsed.pathname}};}
