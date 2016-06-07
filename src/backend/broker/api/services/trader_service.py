from django.http import HttpResponse
from api.models import TraderServer
import json


def query(request):
    params = request.GET
    skip = 0
    count = 20
    q = TraderServer.objects.all()

    result = [item.dict() for item in q]

    return HttpResponse(json.dumps(result), status=200)
