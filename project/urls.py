from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


def rut_roh(request):
    """ Simulates a server error """

    1 / 0


urlpatterns = patterns('backend.views',
                       url(r'^dashboard/', include(admin.site.urls)),
                       url(r'^', include('app.urls')))
