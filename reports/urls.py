from django.conf.urls import url, patterns


urlpatterns = patterns('',
                       url(r'^create/$', 'reports.views.create_report', name="create"),
                       url(r'^edit/(?P<id>\d+)$', 'reports.views.edit_report', name="edit"),
                       url(r'^delete/(?P<id>\d+)$', 'reports.views.delete_report', name="delete"),
                       url(r'^(?P<id>\d+)/$', 'reports.views.reports', name='reports'),
                       )