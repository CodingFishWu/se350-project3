from django.db import models
from django.utils import timezone
import json

# Create your models here.


class OrderInCache:
    def __init__(self, args):
        self.id = args['id']
        self.order_id = args['order_id']        # from trader
        self.trader_ip = args['trader_ip']      # for broadcast purpose
        self.product_code = args['product_code']
        self.s_b = args['s_b']                  # sell or buy
        self.type = args['type']
        self.status = args['status']
        self.amount = args['amount']
        self.price = args['price']
        self.remain = args['remain']

    def json(self):
        result = self.__dict__.copy()
        return json.dumps(result)


class Order(models.Model):
    order_id = models.IntegerField(default=0)
    trader_ip = models.CharField(max_length=20)
    product_code = models.CharField(max_length=30)
    s_b = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    amount = models.FloatField()
    price = models.FloatField()
    remain = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    def json(self):
        return json.dumps(self.dict())

    def dict(self):
        result = self.__dict__.copy()
        if '_state' in result:
            result.pop('_state')
        result["created_time"] = result["created_time"].timestamp()
        return result

    class Meta:
        db_table = 'order'


class CompletedOrder(models.Model):
    completed_order_id = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def json(self):
        return json.dumps(self.dict())

    def dict(self):
        result = self.__dict__.copy()
        if '_state' in result:
            result.pop('_state')
        return result

    class Meta:
        db_table = 'completed_order'


class Product(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=30, unique=True)
    unit = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def json(self):
        return json.dumps(self.dict())

    def dict(self):
        result = self.__dict__.copy()
        if '_state' in result:
            result.pop('_state')
        return result

    class Meta:
        db_table = 'product'


class Transaction(models.Model):
    order1_id = models.IntegerField(default=0)
    order2_id = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(default='trade', max_length=10)
    price = models.FloatField()
    amount = models.FloatField()
    code = models.CharField(default='', max_length=20)

    def json(self):
        return json.dumps(self.dict())

    def dict(self):
        result = self.__dict__.copy()
        if '_state' in result:
            result.pop('_state')
        result["created_time"] = result["created_time"].timestamp()
        return result

    class Meta:
        db_table = 'transaction'


class TraderServer(models.Model):
    ip = models.CharField(max_length=20)
    credits = models.IntegerField(default=0)
    name = models.CharField(max_length=20, default='')

    def json(self):
        return json.dumps(self.dict())

    def dict(self):
        result = self.__dict__.copy()
        if '_state' in result:
            result.pop('_state')
        return result

    class Meta:
        db_table = 'trader_server'
