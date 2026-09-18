// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-434: Unrestricted Upload of File with Dangerous Type
<?php
function save_upload(array $file,string $root):string{$target=$root.'/'.$file['name'];move_uploaded_file($file['tmp_name'],$target);return $target;} // VULNERABLE_SINK
