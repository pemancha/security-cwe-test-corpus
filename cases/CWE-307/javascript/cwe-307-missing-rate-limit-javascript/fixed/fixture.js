// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-307: Improper Restriction of Excessive Authentication Attempts
export function login(store,limiter,user,password){ if(!limiter.allow(user)) throw new Error('rate limited'); return store.verify(user,password); }
