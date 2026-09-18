// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-330: Use of Insufficiently Random Values
import crypto from 'node:crypto';
export const resetToken=()=>crypto.randomBytes(32).toString('base64url');
