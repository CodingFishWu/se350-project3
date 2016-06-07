from django.http import HttpResponse
from api.models import Order, Transaction
import json
from django.core.cache import cache, caches
from api.services import transaction_service, market_depth_service


def query(request):
    params = request.GET
    skip = 0
    count = 20
    q = Order.objects.all()
    q = q.order_by('-created_time')
    if 'code' in params:
        q = q.filter(product_code=params['code'])
    if 'type' in params:
        q = q.filter(type=params['type'])
    if 'status' in params:
        q = q.filter(status=params['status'])

    if 'skip' in params:
        skip = int(params['skip'])
    if 'count' in params:
        count = int(params['count'])
    q = q.filter()[skip: count+skip]

    result = [item.dict() for item in q]
    return HttpResponse(json.dumps(result), status=200)


def create(request):
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    order = Order(**{
        'trader_ip': body['ip'],
        'order_id': body['order_id'],
        'product_code': body['code'],
        's_b': body['s_b'],
        'price': body['price'],
        'type': body['type'],
        'status': 'created',
        'amount': body['amount'],
        'remain': body['amount']
    })
    # first: save to db
    order.save()

    # second: judge the type of the order
    if order.type == 'market':
        execute_market_order(order)
    elif order.type == 'limit':
        execute_limit_order(order)
    elif order.type == 'stop':
        execute_stop_order(order)
    elif order.type == 'cancel':
        execute_cancel_order(order)

    # third: return OK
    return HttpResponse(status=200)


#########################
# important service
#########################


def execute_market_order(order, order_type='trade'):
    s_b = 'sell'
    if order.s_b == 'sell':
        s_b = 'buy'
    product_code = order.product_code

    # first: get market depth and sort
    market_depth = market_depth_service.get_market_depth(s_b, product_code)
    sorted_market_depth = sorted(market_depth, key=lambda market_item: market_item.price, reverse=(order.s_b == 'sell'))

    # second: select the same amount of order to execute the transaction
    for item in sorted_market_depth:
        transaction_service.execute_limit_market_transaction(order, item, order_type=order_type)
        # if all the amount is finished
        if order.remain == 0:
            break
    # if the products on sale are not enough, do nothing
    if order_type == 'stop':
        pass
    else:
        transaction_service.save_completed_order(order.id)


# will then be executed by scheduled task
def execute_stop_order(order):
    stop_cache = caches['stop']
    stop_cache.set(get_key(order), order, timeout=None)
    transaction_service.save_completed_order(order.id)


def execute_cancel_order(order):
    transaction_service.execute_cancel_transaction(order)


def execute_limit_order(order):
    # get all the correspond key in cache
    s_b = 'sell'
    if order.s_b == 'sell':
        s_b = 'buy'
    product_code = order.product_code
    keys = cache.iter_keys(s_b + '-' + product_code + '-' + '*')
    for key in keys:
        value = cache.get(key)
        print(value.dict())
        # the seller's price < buyer's price
        print(key)
        if value.s_b == 'sell' and value.price <= order.price and value.remain > 0:
            transaction_service.execute_limit_market_transaction(order, value)
        elif value.s_b == 'buy' and value.price >= order.price and value.remain > 0:
            transaction_service.execute_limit_market_transaction(order, value)
        if order.remain == 0:
            break

    # the new order hasn't be done
    if order.remain != 0:
        cache.add(get_key(order), order, timeout=None)
    else:
        transaction_service.save_completed_order(order.id)


def trigger_stop_order(code, price):
    stop_cache = caches['stop']
    stop_keys = stop_cache.keys('*-' + code + '-*')
    for stop_key in stop_keys:
        stop_order = stop_cache.get(stop_key)
        if (stop_order.s_b == 'sell' and stop_order.price >= price) or (stop_order.s_b == 'buy' and stop_order.price <= price):
            execute_market_order(stop_order, order_type='stop')
            if stop_order.remain == 0:
                stop_cache.delete(stop_key)
                transaction_service.save_completed_order(stop_order.id)
            else:
                stop_cache.set(get_key(stop_order), stop_order, timeout=None)


def get_key(order):
    return order.s_b + '-' + order.product_code + '-' + str(order.id)
