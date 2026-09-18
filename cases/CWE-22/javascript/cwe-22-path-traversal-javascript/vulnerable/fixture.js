// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-22: Improper Limitation of a Pathname to a Restricted Directory
import fs from 'node:fs';
import path from 'node:path';
export const readFile = name => fs.readFileSync(path.join('/srv/data', name), 'utf8'); // VULNERABLE_SINK
