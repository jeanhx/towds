from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from .views import *

admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^listing/$', Listings, name='listing'),
)


