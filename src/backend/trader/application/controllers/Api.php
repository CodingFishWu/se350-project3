<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Api extends CI_Controller {

	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see https://codeigniter.com/user_guide/general/urls.html
	 */
	private function sendOrder($broker,$item) {
		echo json_encode($item);
		$result = Requests::post($broker.'/order',array('Content-Type' => 'application/json'),json_encode($item));
		var_dump($result->body);
	}

	public function index()
	{
		$this->load->view('welcome_message');
	}

  public function item() {
		header('Access-Control-Allow-Origin:*');
		$this->load->library('PHPRequests');
    $result = Requests::get('http://45.32.12.77:8080/product');
    echo $result->body;
  }

	public function get_order() {
		header('Access-Control-Allow-Origin:*');
		$this->load->model('order_model');
		$order = $this->order_model->get();
		echo $order;
	}

	public function test() {
		$this->load->library('PHPRequests');
		header('Access-Control-Allow-Origin:*');
		header("Access-Control-Allow-Methods", "GET,POST");
		$field = $this->input->post(NULL,TRUE);
		var_dump($field);
	}

	public function add_order() {
		header('Access-Control-Allow-Origin:*');
		header("Access-Control-Allow-Methods", "POST");
		$broker = array('http://104.199.165.224:8000','http://104.199.161.112:8000');
		$this->load->library('PHPRequests');
		$this->load->model('order_model');
		$field = $this->input->post(NULL,TRUE);
		$order = $this->order_model->add($field);
		$amount = $field['amount'];
		$divide = 1;
		$per = $amount;
		if ($amount > 100) {
			$divide = 4;
			$per = ceil($amount/$divide);
			for ($i = 0;$i < $divide;$i++) {
				$orderItem = array(
					'o_id' => $order,
					'status' => 'created',
					'price' => $field['price'],
				);
				if ($amount <= $per) {
					$orderItem['amount'] = $amount;
					$orderItem['remain'] = $amount;
				} else {
					$orderItem['amount'] = $per;
					$orderItem['remain'] = $per;
				}
				$orderItem['broker'] = $broker[array_rand($broker)];
				$item_id = $this->order_model->add_item($orderItem);
				$sendItem = array(
					'ip' => "192.241.193.159",
					'order_id' => $item_id,
					'code' => $field['product_code'],
					's_b' => $field['s_b'],
					'price' => (float)$orderItem['price'],
					'type' => $field['type'],
					'amount' => $orderItem['amount']
				);
				$this->sendOrder($orderItem['broker'],$sendItem);
			}
		} else {
			$orderItem = array(
				'o_id' => $order,
				'status' => 'created',
				'price' => $field['price'],
				'amount' => $field['amount'],
				'remain' => $field['amount'],
				'broker' => $broker[array_rand($broker)]
			);
			$item_id = $this->order_model->add_item($orderItem);
			$sendItem = array(
				'ip' => "192.241.193.159",
				'order_id' => $item_id,
				'code' => $field['product_code'],
				's_b' => $field['s_b'],
				'price' => (float)$orderItem['price'],
				'type' => $field['type'],
				'amount' => (float)$orderItem['amount']
			);
			$this->sendOrder($orderItem['broker'],$sendItem);
		}
		echo "success";
	}

	public function cancel_order() {
		header('Access-Control-Allow-Origin:*');
		header("Access-Control-Allow-Methods", "POST");
		$field = $this->input->post(NULL,TRUE);
		$this->db->where('id',$field['oid']);
		$this->db->update('order_group',array('status'=>canceled));
		$this->db->where('id',$field['oid']);
		$query = $this->db->get('order_group')->result();
		$order = $query[0];

		$this->db->where('o_id',$field['oid']);
		$query = $this->db->get('order_item');
		foreach ($query->result() as $row) {
			$sendItem = array(
				'ip' => "192.241.193.159",
				'order_id' => $row->id,
				'code' => $order->code,
				's_b' => $order->s_b,
				'price' => 0,
				'type' => 'cancel',
				'amount' => 0
			);
			$this->sendOrder($row->broker,$sendItem);
		}
		return 1;
	}

	public function get_transaction() {
		header('Access-Control-Allow-Origin:*');
	}

	public function add_transaction() {
		header('Access-Control-Allow-Origin:*');
		header("Access-Control-Allow-Methods", "POST");
		$field = $this->input->post(NULL,TRUE);
		$this->load->model('trans_model');
		$this->load->model('order_model');
		$data = array(
			'type' => $field['type'],
			'o_id' => $field['order_id'],
			'amount' => $field['number'],
			'price' => $field['price']
		);
		$this->trans_model->add($data);
		if ($field['type'] == "cancel") {
			$this->order_model->cancel($field['order_id']);
		} else {
			$this->order_model->trade($data);
		}
		return 1;
	}
}
