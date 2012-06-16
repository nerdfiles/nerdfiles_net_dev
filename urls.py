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

  #url(r'lastfm/', 'lastfm.views.lastfm_data', name='lastfm'),

  # == admin dashboard == #
  url(r'^dashboard/', include(admin.site.urls)),
  url(r'^dashboard/doc/', include('django.contrib.admindocs.urls')),  
  url(r'^', include('cms.urls')),
)


# == LOCAL ======================================== #

urlpatterns = patterns('',
  url(r'^_assets(?P<path>.*)$', 'django.views.static.serve',
  {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  url(r'^_static(?P<path>.*)$', 'django.views.static.serve',
  {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
  url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

handler404 = 'views.error_404'
handler500 = 'views.error_500'

