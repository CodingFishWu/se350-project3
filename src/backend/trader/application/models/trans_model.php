<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Trans_model extends CI_Model {

    function __construct()
    {
        parent::__construct();
    }

    function get($code) {
      $this->db->select('order_group.s_b,transaction.price,transaction.amount,transaction.create_time');
      $this->db->where('order_group.product_code',$code);
      $this->db->where('transaction.type','trade');
      $this->db->join('order_item','order_item.id = transaction.o_id');
      $this->db->join('order_group','order_item.o_id = order_group.id');
      $query = $this->db->get('transaction');
      return $query->result();
    }

    function add($field) {
      date_default_timezone_set('PRC');
      $field['create_time'] = date('Y-m-d H:i:s');
      $this->db->insert('transaction',$field);
      return $this->db->insert_id();
    }

}
