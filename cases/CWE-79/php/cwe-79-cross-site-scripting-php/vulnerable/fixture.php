// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-79: Improper Neutralization of Input During Web Page Generation
<?php
function render_profile(string $name): string { return '<h1>'.$name.'</h1>'; } // VULNERABLE_SINK
