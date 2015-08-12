from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    template_name = 'login.html'
    context = {'template_title': 'towds---------- hello'}

    return render(request, template_name, context)
