### user

for login purpose

| field    | type   | description |
| -------- | ------ | ----------- |
| id       | Int    |
| password | String |

### product

predefined product(in our case, it is defined by broker)

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| name       | String |
| code       | String |
| unit       | String |
| type       | String |
| is_deleted  | boolean| check if it is deleted |

### order

4 types order

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| s_b        | String | 'sell' or 'buy' |
| type       | String |'market' or 'limit' or 'stop' or 'cancel' |
| status     | String |'finish', 'pending', 'cancel' |
| product_code| String|
| amount     | double | 
| price      | double | wondered price |
| remain     | double | remain amount of order |
| created_time| Date   |

### transaction

to describe a deal

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| order_id   | Int    |
| created_time| Date   |
| price      | double |
| amount     | double |
