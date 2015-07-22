#
# Licensed Materials - Property of esse.io
#
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.forms.widgets import flatatt
from base import ZenWidget


class ContentWrapper(ZenWidget):
    _content_header = None
    _content = None

    def __init__(self):
        super(self.__class__, self).__init__("div",
                                             {"class": "content-wrapper"})

    def set_content_header(self, content_header):
        self._content_header = content_header

    def set_content(self, content):
        self._content = content

    def render(self):
        if self._content_header:
            self.append_widget(self._content_header)
        if self._content:
            self.append_widget(self._content)
        return super(self.__class__, self).render()
