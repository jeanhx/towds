from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

def make_listing(request):

    template_name = "make_ad.html"

    context = {'template_title': 'towds---------- make ad~'}

    if request.POST:
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.save()
            context['id'] = listing.id

    else:
        form = ListingForm()

    context['form'] = form
    context.update(csrf(request))

    return render(request, template_name, context)


def show_listing(request, id):

    ad = get_object_or_404(Listing, id=id)

    template_name = "show_ad.html"

    context = {
        'template_title': 'towds---------- show ad~',
        'ad': ad
    }

    return render(request, template_name, context)