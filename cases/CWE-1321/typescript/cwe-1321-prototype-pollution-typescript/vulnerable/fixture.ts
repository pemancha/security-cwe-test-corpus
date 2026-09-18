// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-1321: Improperly Controlled Modification of Object Prototype Attributes
export function merge(target:Record<string,unknown>,input:Record<string,unknown>){for(const key in input)target[key]=input[key];return target;} // VULNERABLE_SINK
