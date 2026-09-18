// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-307: Improper Restriction of Excessive Authentication Attempts
export const login=(store,user,password)=>store.verify(user,password); // VULNERABLE_SINK
