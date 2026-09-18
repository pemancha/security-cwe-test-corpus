// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-352: Cross-Site Request Forgery
export const changeEmail=(session,email)=>session.account.update({email}); // VULNERABLE_SINK
