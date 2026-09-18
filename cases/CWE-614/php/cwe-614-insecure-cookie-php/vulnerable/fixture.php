// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-614: Sensitive Cookie in HTTPS Session Without Secure Attribute
<?php
function session_cookie(string $id):void{setcookie('session',$id,['httponly'=>true,'samesite'=>'Lax']);} // VULNERABLE_SINK
