// CONTROLLED REMEDIATED TEST FIXTURE
// CWE-352: Cross-Site Request Forgery
<?php
function change_email($session,$request,$email){if(!hash_equals($session->csrfToken,$request->csrfToken??'')){throw new RuntimeException('invalid csrf token');}return $session->account->update(['email'=>$email]);}
