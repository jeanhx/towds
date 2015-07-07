import json
from django.http import HttpResponse


def json_error(msg):
	return "{\"error\":\"%s\"}" % msg

def Listing(request):

    return HttpResponse("User profile")
