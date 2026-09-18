// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-78: Improper Neutralization of Special Elements used in an OS Command
import childProcess from 'node:child_process';
export const lookup = host => childProcess.execSync('nslookup ' + host).toString(); // VULNERABLE_SINK
