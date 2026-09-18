// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-79: Improper Neutralization of Input During Web Page Generation
export const renderProfile = name => `<h1>${name}</h1>`; // VULNERABLE_SINK
