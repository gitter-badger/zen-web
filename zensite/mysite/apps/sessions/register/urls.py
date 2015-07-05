from django.conf.urls import patterns, url

urlpatterns = patterns('mysite.apps.sessions.register.views',
    url(r'^$', 'register'),
    url(r'^success/$', 'register_success'),
    url(r'^submit/?$', 'register_submit'),
    url(r'^confirm/$', 'register_confirm'),
)
