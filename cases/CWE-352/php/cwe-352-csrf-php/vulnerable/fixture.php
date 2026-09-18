// CONTROLLED SECURITY TEST FIXTURE: DO NOT DEPLOY
// CWE-352: Cross-Site Request Forgery
<?php
function change_email($session,$email){return $session->account->update(['email'=>$email]);} // VULNERABLE_SINK
