from django.conf.urls.defaults import *
from django.conf import settings

# admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nerdfiles_net_dev.views.home', name='home'),
    # url(r'^nerdfiles_net_dev/', include('nerdfiles_net_dev.foo.urls')),
    
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^semantic/', include('semanticeditor.urls')),
    
    # django cms
    url(r'^', include('cms.urls')),
    #url(r'_assets/', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns