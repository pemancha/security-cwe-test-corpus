// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-22: Improper Limitation of a Pathname to a Restricted Directory
import fs from 'node:fs';
import path from 'node:path';
const base = path.resolve('/srv/data');
export function readFile(name) { const candidate = path.resolve(base, name); if (!candidate.startsWith(base + path.sep)) throw new Error('invalid path'); return fs.readFileSync(candidate, 'utf8'); }
