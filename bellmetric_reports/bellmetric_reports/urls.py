from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    # Reports
    url(r'^report/', include(
    	'reports.urls',
    	namespace='reports')
    ),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
