from django.conf.urls import patterns, include, url
from django.contrib import admin
# from views import ScoreCreate

urlpatterns = patterns('',
    # url(r'^score/', ScoreCreate.as_view(), name='score'),
    url(r'^score/list/', 'risk_evidence.views.score_list', name='score_list'),
    url(r'^score/add', 'risk_evidence.views.score_add', name='add_score'),
    url(r'^score/edit/(\d+)/$', 'risk_evidence.views.score_edit', name='edit_score'),
    url(r'^supply_chain_impact/$', 'risk_evidence.views.sci_list', name='sci_list'),
    url(r'^supply_chain_impact/(.+)/$', 'risk_evidence.views.sci_list_country', name='sci_list_country'),
    url(r'^probability/$', 'risk_evidence.views.probability_list', name='probability_list'),
    url(r'^probability/(.+)/$', 'risk_evidence.views.probability_list_country', name='probability_list_country'),
    # url(r'^supply_chain_impact/add', 'risk_evidence.views.evidence_add', name="evidence_add"),
    url(r'^evidence/add', 'risk_evidence.views.evidence_add', name="evidence_add"),
    url(r'^overview/', 'risk_evidence.views.overview', name='overview'),
    url(r'^visual_map', 'risk_evidence.views.visual_map', name='visual_map'),
    url(r'^hypothesis_list', 'risk_evidence.views.hypothesis_list', name='hypothesis_list'),
    url(r'^evidence/edit/(\d+)/$', 'risk_evidence.views.evidence_edit', name='evidence_edit'),
    url(r'^logout', 'risk_evidence.views.user_logout', name='logout'),
    url(r'^login', 'risk_evidence.views.user_login', name='login'),
)
