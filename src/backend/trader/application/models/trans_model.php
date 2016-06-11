<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Trans_model extends CI_Model {

    function __construct()
    {
        parent::__construct();
    }

    function get() {

    }

    function add($field) {
      date_default_timezone_set('PRC');
      $field['create_time'] = date('Y-m-d H:i:s');
      $this->db->insert('transaction',$field);
      return $this->db->insert_id();
    }

}
