// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-601: URL Redirection to Untrusted Site
export const redirect=next=>({status:302,headers:{location:next}}); // VULNERABLE_SINK
