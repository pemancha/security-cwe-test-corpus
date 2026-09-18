// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-614: Sensitive Cookie in HTTPS Session Without Secure Attribute
export const sessionCookie=id=>`session=${id}; Secure; HttpOnly; SameSite=Lax`;
