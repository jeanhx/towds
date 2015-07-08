import json
from django.http import HttpResponse
from .models import Listing

def json_error(msg):
	return "{\"error\":\"%s\"}" % msg


def Listing(request):

    return HttpResponse("User profile")


def get_listing(request, listing_id):
    listing = Listing,objects.get(id=listing_id)

    return HttpResponse(Listing)

