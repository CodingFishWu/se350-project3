from django.http import HttpResponse
from api.services import user_service, order_service, product_service, market_depth_service, transaction_service, trader_service


def login(request):
    if request.method == 'POST':
        return user_service.login(request)
        pass
    else:
        return HttpResponse(status=405)


def sign(request):
    if request.method == 'POST':
        return user_service.signup(request)
    else:
        return HttpResponse(status=405)


def order(request):
    if request.method == 'GET':
        return order_service.query(request)
    if request.method == 'POST':
        return order_service.create(request)
    else:
        return HttpResponse(status=405)


def product(request):
    if request.method == 'GET':
        return product_service.query(request)
    else:
        return HttpResponse(status=405)


def market_depth(request, code):
    if request.method == 'GET':
        return market_depth_service.query(request, code)
    else:
        return HttpResponse(status=405)


def transaction(request):
    if request.method == 'GET':
        return transaction_service.query(request)
        pass
    else:
        return HttpResponse(status=405)


def trader(request):
    if request.method == 'GET':
        return trader_service.query(request)
    else:
        return HttpResponse(status=405)