// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-94: Improper Control of Generation of Code
export const calculate = expression => eval(expression); // VULNERABLE_SINK
