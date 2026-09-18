// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-79: Improper Neutralization of Input During Web Page Generation
<?php
function render_profile(string $name): string { return '<h1>'.htmlspecialchars($name, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8').'</h1>'; }
