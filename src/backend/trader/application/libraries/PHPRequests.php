<?php
if (!defined('BASEPATH')) exit('No direct script access allowed');
require_once dirname(__FILE__)."/../third_party/Requests-1.6.0/library/Requests.php";
class PHPRequests {
    public function __construct() {
       Requests::register_autoloader();
    }
}
