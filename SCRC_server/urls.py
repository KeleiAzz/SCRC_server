from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SCRC_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'query.views.home_page', name='home'),
    url(r'query/', include('query.urls')),
    # url(r'risk_evidence/', include('risk_evidence.urls')),
    # url(r'^companies/(.+)/$', 'query.views.company_details', name='company_details'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^advanced_search/', 'query.views.advanced_search', name='advanced_search'),
    # url(r'^basic_search/', 'query.views.basic_search', name='basic_search'),
    # url(r'^evidence_list/', 'query.views.evidence_list', name='evidence_list'),

)
