from django.core.cache import caches, cache
from django.utils import timezone
from api.services import market_depth_service, order_service
import logging
import django.utils.timezone

logger = logging.getLogger(__name__)


def execute_stop_order():
    logging.info("in scheduled jobs" + str(timezone.now()))
    stop_cache = caches['stop']
    stop_keys = stop_cache.keys('*')
    for stop_key in stop_keys:
        stop_order = stop_cache.get(stop_key)
        s_b = 'sell'
        if stop_order.s_b == 'sell':
            s_b = 'buy'
        product_code = stop_order.product_code
        # first: get market depth and sort
        market_depth = market_depth_service.get_market_depth(s_b, product_code)
        sorted_market_depth = sorted(market_depth, key=lambda market_item: market_item.price,
                                     reverse=(stop_order.s_b == 'sell'))
        if len(sorted_market_depth) > 0 and \
                ((stop_order.s_b == 'sell' and sorted_market_depth[0].price < stop_order.price) or
                    (stop_order.s_b == 'buy' and sorted_market_depth[0].price > stop_order.price)):
            order_service.execute_market_order(stop_order)
            if stop_order.remain == 0:
                stop_cache.delete(stop_key)
            else:
                stop_cache.set(stop_key, stop_order, timeout=None)


def test():
    stop_cache = caches['stop']
    stop_cache.set(str(timezone.now()), 'test', timeout=None)
