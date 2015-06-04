from django.conf.urls import patterns, include, url
from django.contrib import admin
# from views import ScoreCreate

urlpatterns = patterns('',
    # url(r'^score/', ScoreCreate.as_view(), name='score'),
    url(r'^score/list/', 'risk_evidence.views.score_list', name='score_list'),
    url(r'^score/add', 'risk_evidence.views.add_score', name='add_score'),
    url(r'^score/edit/(\d+)/$', 'risk_evidence.views.edit_score', name='edit_score'),
)
