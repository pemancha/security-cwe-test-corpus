// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-614: Sensitive Cookie in HTTPS Session Without Secure Attribute
export const sessionCookie=id=>`session=${id}; HttpOnly; SameSite=Lax`; // VULNERABLE_SINK
