from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = patterns(
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
