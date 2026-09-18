// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
const config={databasePassword:'fixture-only-password'};
export const debugConfig=()=>({...config,databasePassword:'[REDACTED]'});
