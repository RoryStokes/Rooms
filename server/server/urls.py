from django.conf.urls import patterns, include, url
from django.contrib import admin
from server.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^game/', game),
    url(r'^init', init),
    url(r'^start', start),
    url(r'^state', state),
    url(r'^connect/', connect),
    url(r'^admin/', include(admin.site.urls)),
)
