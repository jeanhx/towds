from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from core.views import *

admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', include('core.urls')),
    url(r'^ad/', include('ads.urls')),
    url(r'^api/', include('towds_api.urls')),
    url(r'^dash/', include('profile.urls')),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)

