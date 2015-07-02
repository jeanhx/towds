import json
from django.http import HttpResponse


def json_error(msg):
	return "{\"error\":\"%s\"}" % msg

def Listing(request):

    try:
        request = request
        request = "ok"
        return HttpResponse(request)

    except error:
        return HttpResponse(json_error(error))
