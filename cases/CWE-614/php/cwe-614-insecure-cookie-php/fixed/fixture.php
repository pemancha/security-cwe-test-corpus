// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-614: Sensitive Cookie in HTTPS Session Without Secure Attribute
<?php
function session_cookie(string $id):void{setcookie('session',$id,['secure'=>true,'httponly'=>true,'samesite'=>'Lax']);}
