from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (CallsListView, SourceListView)

urlpatterns = patterns('',
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
