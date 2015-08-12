import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ads.models import Listing



def Dash(request):

    if request.POST:
        template_name = 'dash.html'
        context = {'template_title': 'towds---------- dashboard~'}

        input_lat = request.POST['lat']
        input_lon = request.POST['lon']

        context['lat'] = input_lat
        context['lon'] = input_lon

        Listing.objects.filter(lon__gt=(input_lon-1.0),
                               lon__lt=(input_lon+1.0),
                               lat__gt=(input_lat-1.0),
                               lat__lt=(input_lat+1.0))[:10]

        return render(request, template_name, context)

    else:
        return HttpResponseRedirect('/')

