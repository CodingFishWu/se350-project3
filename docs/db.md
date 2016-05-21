### user

for login purpose

| field    | type   | description |
| -------- | ------ | ----------- |
| id       | Int    |
| password | String |
| type     | String |'trader' or 'broker'|

### product

predefined product(in our case, it is defined by broker)

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| name       | String |
| code       | String |
| unit       | String |
| type       | String |
| isDeleted  | boolean| check if it is deleted |

### order

4 types order

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| trader_id  | Int    |
| detail_id  | Int    | foreign key of order_detial|
| s_b        | String | 'sell' or 'buy' |
| type       | String |'market' or 'limit' or 'stop' or 'cancel' |
| status     | String |'finish', 'pending', 'cancel' |
| product_id | Int    |
| amount     | double | 
| stop_price | double | height price(used for stop order)|
| price      | double | wondered price |
| remain     | double | remain amount of order |
| createdTime| Date   |

### transaction

to describe a deal

| field      | type   | description |
| ---------- | ------ | ----------- |
| id         | Int    |
| order_id   | Int    |
| createdTime| Date   |
| price      | double |
| amount     | double |
