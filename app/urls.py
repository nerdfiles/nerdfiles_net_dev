from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

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

urlpatterns += patterns(
    'app',

    # url(r'^$', 'views.HomeView', name='home'),
    url(r'^addresses$', views.AddressList.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[0-9]+)$', views.AddressDetail.as_view(
    ), name='address-detail'),

    url(r'^users$', views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(
    ), name='user-detail'),

    url(r'__/recent-tracks/', 'views.lastfm_recent_tracks',
        name='lastfm_recent_tracks'),
)

urlpatterns += patterns('',
                        url(r'^api-token-auth/',
                            'rest_framework.authtoken.views.obtain_auth_token')
                        )

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
