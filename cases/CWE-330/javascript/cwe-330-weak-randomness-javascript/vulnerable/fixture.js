// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-330: Use of Insufficiently Random Values
export const resetToken=()=>String(Math.random()); // VULNERABLE_SINK
