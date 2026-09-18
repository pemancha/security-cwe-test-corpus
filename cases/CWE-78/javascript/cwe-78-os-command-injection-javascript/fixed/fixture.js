// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-78: Improper Neutralization of Special Elements used in an OS Command
import childProcess from 'node:child_process';
export const lookup = host => childProcess.execFileSync('nslookup', [host], {encoding:'utf8'});
