import json
from django.http import HttpResponse
from googlemaps import GoogleMaps

def json_error(msg):
	return "{\"error\":\"%s\"}" % msg

def Base(request):
    gmaps = GoogleMaps(API_KEY)
    lat, lng = gmaps.address_to_latlng(address)
    return HttpResponse("User Lat,Lon: %s,%s" % (lat,lng))
