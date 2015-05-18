from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SCRC_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'query.views.home_page', name='home'),
    url(r'^companies/(.+)/$', 'query.views.company_details', name='company_details'),
    url(r'^admin/', include(admin.site.urls)),
)
