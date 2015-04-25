from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
import views

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
admin.autodiscover()

handler500 = 'app.views.error_500'
handler404 = 'app.views.error_404'


urlpatterns = patterns(
    '',


    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),

    url(r'__/recent-tracks/', views.lastfm_recent_tracks,
        name='lastfm_recent_tracks'),
    url(r'^dashboard/', include(admin.site.urls)),


    #url(r'^$', 'views.HomeView', name='home'),
    url(r'^addresses$', views.AddressList.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[0-9]+)$', views.AddressDetail.as_view(
    ), name='address-detail'),

    url(r'^users$', views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(
    ), name='user-detail'),

    url(r'^api-token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),

)

urlpatterns = format_suffix_patterns(urlpatterns)

# Imagestore config
urlpatterns = patterns(
    '',
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
) + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),) + urlpatterns
'''
