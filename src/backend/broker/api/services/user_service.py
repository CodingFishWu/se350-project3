from django.http import HttpResponse
from api.models import Product
from http.client import HTTPSConnection
from api.utils import myExceptions
import json


def login(request):
    try:
        conn = HTTPSConnection('ip.oauth')
        conn.request('POST', '/oauth')
        r1 = conn.getresponse()
        if r1.status == 200:
            access_token = r1.read()
        else:
            raise myExceptions.OauthError('password error')
        return HttpResponse(status=200)

    except myExceptions.OauthError as e:
        return HttpResponse(json.dumps({'message': e.value}), status=403)


def signup(request):
    # decoder
    body = request.body.decode('utf-8')
    print(request.GET['a'])
    print(type(request.GET['a']))

    print(json.loads(body))
    product = Product(**json.loads(body))
    # print(request.POST['name'])
    # print(type(request.POST['name']))
    print(product.name)
    # product.save()

    return HttpResponse(status=201)
