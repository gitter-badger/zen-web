#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

from django.conf.urls import patterns, url

urlpatterns = patterns('zensite.apps.sessions.login.views',
    url(r'^$', 'login'),
    url(r'^submit/?$', 'login_submit'),
)
