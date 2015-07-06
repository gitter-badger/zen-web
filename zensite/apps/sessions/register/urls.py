#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

from django.conf.urls import patterns, url

urlpatterns = patterns('zensite.apps.sessions.register.views',
    url(r'^$', 'register'),
    url(r'^success/$', 'register_success'),
    url(r'^submit/?$', 'register_submit'),
    url(r'^confirm/$', 'register_confirm'),
)
