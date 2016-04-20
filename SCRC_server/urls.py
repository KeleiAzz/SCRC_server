from django.conf.urls import patterns, include, url
from django.contrib import admin
from risk_evidence import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'SCRC_server.views.home', name='home'),
                       url(r'^$', 'risk_evidence.views.home', name='home'),
                       url(r'query/', include('query.urls')),
                       url(r'risk_evidence/', include('risk_evidence.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/', views.user_login, name='login'),
                       url(r'^logout/', views.user_logout, name='logout'),
                       url(r'^accounts/login/', views.user_login, name='login'),
                       )
