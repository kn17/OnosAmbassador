from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^(?P<event_id>\d+)/$', 'events.views.event'),
                       url(r'^create/$', 'events.views.create_event', name='create'),
                       )