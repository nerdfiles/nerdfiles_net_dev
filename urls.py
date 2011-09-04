from django.conf.urls.defaults import patterns, include, url

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
)
