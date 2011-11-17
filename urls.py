# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to


# == ADMIN ======================================== #

admin.autodiscover()


# == UTIL ======================================== #

def rut_roh(request):
  """ Simulates a server error """
  1/0
    

# == URLPATTERNS ======================================== #

urlpatterns = patterns('',
  (r'^rut-rot/$', rut_roh),
  # == admin dashboard == #
  url(r'^dashboard/', include(admin.site.urls)),
  url(r'^dashboard/doc/', include('django.contrib.admindocs.urls')),  
  url(r'^', include('cms.urls')),
)


# == LOCAL ======================================== #

if settings.LOCAL_DEVELOPMENT:
  urlpatterns = patterns('',
    url(r'^'+settings.ASSETS_URL+'(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
  ) + urlpatterns

handler404 = 'nerdfiles_net_dev.views.error_404'
handler500 = 'nerdfiles_net_dev.views.error_500'

