<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Order_model extends CI_Model {

    function __construct()
    {
        parent::__construct();
    }

    function get() {
      $result = array();
      $this->db->order_by('id desc');
      $query = $this->db->get('order_group');
      foreach ($query->result() as $row) {
        $temp = new stdClass();
        $temp->order = $row;
        $this->db->where('o_id',$row->id);
        $q = $this->db->get('order_item');
        $temp->item = $q->result();
        array_push($result,$temp);
      }
      return json_encode($result);
    }

    function add($field) {
      date_default_timezone_set('PRC');
      $field['created_time'] = date('Y-m-d H:i:s');
      $field['status'] = 'created';
      $field['remain'] = $field['amount'];
      $this->db->insert('order_group',$field);
      return $this->db->insert_id();
    }

    function add_item($field) {
      $this->db->insert('order_item',$field);
      return $this->db->insert_id();
    }

    function cancel($id) {
      $data = array('status'=>'canceled');
      $this->db->where('id',$id);
      $this->db->update('order_item',$data);
    }

    function trade_group($id,$amount) {
      $this->db->where('id',$id);
      $query = $this->db->get('order_group')->result();
      $order = $query[0];

      if ($order->remain > $amount) {
        $this->db->where('id',$id);
        $this->db->update('order_group',array('remain'=>$order->remain-$amount));
      } else {
        $this->db->where('id',$id);
        $this->db->update('order_group',array('remain'=>0,'status'=>'finished'));
      }
    }

    function trade($field) {
      $this->db->where('id',$field['o_id']);
      $query = $this->db->get('order_item')->result();
      $order = $query[0];

      if ($order->remain > $field['amount']) {
        $this->db->where('id',$field['o_id']);
        $this->db->update('order_item',array('remain'=>$order->remain-$field['amount']));
      } else {
        $this->db->update('order_item',array('remain'=>0,'status'=>'finished'));
      }
      $this->trade_group($order->o_id,$field['amount']);
    }
}
