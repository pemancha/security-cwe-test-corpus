// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-79: Improper Neutralization of Input During Web Page Generation
const escapeHtml = value => value.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const renderProfile = name => `<h1>${escapeHtml(name)}</h1>`;
