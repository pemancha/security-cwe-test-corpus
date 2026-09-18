// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-94: Improper Control of Generation of Code
export function calculate(expression) { if (!/^[0-9 +.-]+$/.test(expression)) throw new Error('invalid expression'); const parts=expression.trim().split(/\s+/); if (parts.length!==3) throw new Error('unsupported'); const [a,op,b]=parts; if(op==='+') return Number(a)+Number(b); if(op==='-') return Number(a)-Number(b); throw new Error('unsupported'); }
