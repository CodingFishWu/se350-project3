#### broker
- GET: /marketDepth
- POST: /order
`
  {
    amount, order_id, code, s_b, price, ip, type
  }
`

#### trader
- POST: /transaction
`
  {
    transaction_id, order_id, number, price
  }
`