from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from towards.towds.models import Lister


def Home(request):
    template_name = core/dash.html

    user = None
    if request.user.is_authenicated():
        user = request.user

    else:
        return HttpResponse("Error: not logged in")


    context = {'user': user}

     
    return render(request, template_name, context)
