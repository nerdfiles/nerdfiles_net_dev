# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
#from django.views.generic.simple import redirect_to
from views import *


# == ADMIN ======================================== #

admin.autodiscover()


# == UTIL ======================================== #

def rut_roh(request):
  """ Simulates a server error """
  1/0


# == URLPATTERNS ======================================== #

urlpatterns = patterns('',
  url(r'^rut-rot/$', rut_roh),

  url(r'^dashboard/cache/', include('django_memcached.urls')),

  url(r'__/recent-tracks/', 'views.lastfm_recent_tracks', name='lastfm_recent_tracks'),
  url(r'__/recent-tweets/', 'views.twitter_recent_tweets', name='twitter_recent_tweets'),
  url(r'lastfm/', 'lastfm.views.lastfm_data', name='lastfm'),

  url(r'tumblr/', 'views.tumblr_redirect', name='tumblr'),

  #url(r'web-cv/', 'views.web_cv', name='web_cv'),

  # == admin dashboard == #

  url(r'^dashboard/', include(admin.site.urls)),

  url(r'^dashboard/doc/', include('django.contrib.admindocs.urls')),

  url(r'^', include('cms.urls')),

)

urlpatterns = patterns('',

  url(r'^assets(?P<path>.*)$', 'django.views.static.serve',
  {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

  url(r'^_static(?P<path>.*)$', 'django.views.static.serve',
  {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

  url(r'', include('django.contrib.staticfiles.urls')),

) + urlpatterns

#urlpatterns = patterns(
    #'',
    #url(r'^_assets/(?P<path>.*)$', 'django.views.static.serve',
        #{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#) + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = patterns(
    #'',
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        #{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
#) + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# == LOCAL ======================================== #

handler404 = 'views.error_404'
handler500 = 'views.error_500'


