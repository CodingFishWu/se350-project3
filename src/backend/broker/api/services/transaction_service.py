from django.http import HttpResponse
from http.client import HTTPSConnection, HTTPConnection
from api.models import Transaction, CompletedOrder, Order
from api.services import market_depth_service, order_service
from django.core.cache import cache, caches
import json


def query(request):
    params = request.GET
    skip = 0
    count = 20

    q = Transaction.objects.all()
    q = q.order_by('-created_time')
    if 'type' in params:
        q = q.filter(type=params['type'])
    if 'code' in params:
        q = q.filter(code=params['code'])
    if 'skip' in params:
        skip = int(params['skip'])
    if 'count' in params:
        count = int(params['count'])
    q = q.filter()[skip: count+skip]

    result = [item.dict() for item in q]
    return HttpResponse(json.dumps(result), status=200)


def execute_limit_market_transaction(in_order, order, order_type='trade'):
    order_key = order.s_b + '-' + order.product_code + '-' + str(order.id)
    print(order_key)
    # lock the key
    #  [todo] with cache.lock(order_key + "dd"):
    print(order_key)
    print(order.dict())
    order = cache.get(order_key)
    # if it's done by others
    if order is None:
        return
    price = min(in_order.price, order.price)
    amount = min(in_order.remain, order.remain)
    # update order
    in_order.remain = in_order.remain - amount
    order.remain = order.remain - amount
    if order.remain == 0:
        cache.delete(order_key)
        save_completed_order(order.id)
    else:
        cache.set(order_key, order, timeout=None)

    # create transaction
    transaction = Transaction(**{
        'order1_id': in_order.id,
        'order2_id': order.id,
        'type': 'trade',
        'price': price,
        'amount': amount,
        'code': order.product_code
    })
    transaction.save()

    # solve stop order [todo] have problem
    if order_type == 'trade':
        order_service.trigger_stop_order(order.product_code, price)

    # send transaction to trader
    send_to_trader(in_order.trader_ip, {
        'transaction_id': transaction.id,
        'type': 'trade',
        'order_id': in_order.order_id,
        'trade_firm': order.trader_ip,
        'number': amount,
        'price': price
    })
    send_to_trader(order.trader_ip, {
        'transaction_id': transaction.id,
        'type': 'trade',
        'order_id': order.order_id,
        'trade_firm': in_order.trader_ip,
        'number': amount,
        'price': price
    })
    # [todo] broadcast


def execute_cancel_transaction(order):
    stop_cache = caches['stop']
    left_orders = []

    stop_keys = stop_cache.keys('*')
    is_stop = False
    for stop_key in stop_keys:
        stop_order = stop_cache.get(stop_key)
        if stop_order.order_id == order.order_id:
            left_orders.append(stop_order)
            stop_cache.delete(stop_key)
            save_canceled_order(stop_order.id)
            is_stop = True

    if not is_stop:
        market_depth = market_depth_service.get_market_depth(order.s_b, order.product_code)
        for item in market_depth:
            if item.order_id == order.order_id:
                cache.delete(item.s_b + '-' + item.product_code + '-' + str(item.id))
                save_canceled_order(item.id)
                left_orders.append(item)

    for left_order in left_orders:
        # save transaction
        transaction = Transaction(**{
            'order1_id': order.id,
            'order2_id': 0,
            'type': 'cancel',
            'price': 0,
            'amount': left_order.remain,
            'code': left_order.product_code
        })
        transaction.save()
        # send transaction to trader
        send_to_trader(order.trader_ip, {
            'transaction_id': transaction.id,
            'order_id': order.order_id,
            'type': 'cancel',
            'number': left_order.remain,
            'trade_firm': '',
            'price': 0
        })


def send_to_trader(ip, transaction):
    try:
        conn = HTTPConnection(ip)
        conn.request('POST', '/transaction', json.dumps(transaction))
    except ConnectionError:
        pass


def save_completed_order(id):
    order = Order.objects.get(pk=id)
    order.status = 'finished'
    order.save()
    completed_order = CompletedOrder(completed_order_id=id)
    completed_order.save()


def save_canceled_order(id):
    order = Order.objects.get(pk=id)
    order.status = 'canceled'
    order.save()
