from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^profile/(?P<profile_id>\d+)/$', 'user_profile.views.profile', name ='profile' ),
                       url(r'^update_profile/$', 'user_profile.views.update_profile', name='update'),
                       url(r'^send_update_profile/$', 'user_profile.views.send_update_profile', name='user_profile'),
                       url(r'^create/$', 'user_profile.views.create_profile', name='create'),
                       )