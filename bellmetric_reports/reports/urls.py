from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (CallsListView, SourceListView, ReportsListView)

urlpatterns = patterns('',

    # {% url "reports:report-page" %}
    url(
        regex=r'^$',
        view=ReportsListView.as_view(),
        name="report-page"
    ),
    # {% url "reports:calls" %}
    url(
        regex=r'^calls/$',
        view=CallsListView.as_view(),
        name="calls"
    ),
    # {% url "reports:call-source" call.id %}
    url(
        regex=r'^call/(?P<cdr>\d+)/source/$',
        view=SourceListView.as_view(),
        name="call-source"
    ),
)
