// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-1321: Improperly Controlled Modification of Object Prototype Attributes
const blocked=new Set(['__proto__','prototype','constructor']);
export function merge(target,input){for(const [key,value] of Object.entries(input)){if(blocked.has(key))throw new Error('unsafe key');target[key]=value;}return target;}
