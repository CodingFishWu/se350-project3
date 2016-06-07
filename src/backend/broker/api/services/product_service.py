from django.http import HttpResponse
from api.models import Product
import json


def query(request):
    params = request.GET
    skip = 0
    count = 20
    q = Product.objects.all()

    result = [item.dict() for item in q]

    return HttpResponse(json.dumps(result), status=200)
