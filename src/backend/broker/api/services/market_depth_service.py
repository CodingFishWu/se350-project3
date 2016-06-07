from django.core.cache import cache
from django.http import HttpResponse
import json


def query(request, code):
    result = []
    result.extend([item.dict() for item in get_market_depth('sell', code)])
    result.extend([item.dict() for item in get_market_depth('buy', code)])
    return HttpResponse(json.dumps(result), status=200)


def get_market_depth(s_b, code):
    orders = []
    keys = cache.keys(s_b + '-' + code + '-*')
    for key in keys:
        orders.append(cache.get(key))
    return orders


def get_ordered_market_depth(s_b, code):
    orders = get_market_depth(s_b, code)
    sorted_orders = sorted(orders, key=lambda market_item: market_item.price)
    return sorted_orders


def get_reversed_market_depth(s_b, code):
    orders = get_market_depth(s_b, code)
    sorted_orders = sorted(orders, key=lambda market_item: market_item.price, reverse=True)
    return sorted_orders
