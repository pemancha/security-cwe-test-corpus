// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-434: Unrestricted Upload of File with Dangerous Type
<?php
function save_upload(array $file,string $root):string{$allowed=['text/plain'=>'txt','application/json'=>'json'];$mime=(new finfo(FILEINFO_MIME_TYPE))->file($file['tmp_name']);if(!isset($allowed[$mime]))throw new RuntimeException('type rejected');$target=$root.'/'.bin2hex(random_bytes(16)).'.'.$allowed[$mime];move_uploaded_file($file['tmp_name'],$target);return $target;}
