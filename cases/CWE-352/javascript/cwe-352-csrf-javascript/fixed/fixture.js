// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-352: Cross-Site Request Forgery
export function changeEmail(session,request,email){if(!request.csrfToken||request.csrfToken!==session.csrfToken)throw new Error('invalid csrf token');return session.account.update({email});}
