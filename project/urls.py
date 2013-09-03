from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
admin.autodiscover()


def rut_roh(request):
    """ Simulates a server error """

    1 / 0


urlpatterns = patterns('backend.views',
                       url(r'^rut-rot/$', rut_roh),
                       url(r'^dashboard/cache/', include(
                           'django_memcached.urls')),
                       url(r'^', include('app.urls')))


urlpatterns += patterns('backend.views',
                        url(r'^dashboard/', include(admin.site.urls)),
                        url(r'^', include('cms.urls'))
                        )
