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

from django.forms.widgets import flatatt
from django.forms.widgets import Widget
from django.utils.html import conditional_escape, format_html, html_safe

class ZenWidget(Widget):
    sub_widgets = []
    id = ""
    element_name = ""
    text = ""
    name = ""

    def __init__(self, element_name, name=None, id=None, attrs=None):
        if id:
            self.id = id
        if attrs:
            self.attrs = attrs.copy()
        else:
            self.attrs = {}
        self.element_name = element_name
        if name:
            self.name = name

    def append_child(self, text):
        self.text = text

    def append_widget(self, widget):
        self.sub_widgets.append(widget)

    def render(self):
        final_attrs = self.build_attrs(self.attrs, name=self.name, id=self.id)
        html = "<{}".format(self.element_name)
        html = html + "{}"
        if self.text:
            html = html + " >{}".format(self.text) + "</{}>".format(self.element_name)
        else:
            html = html + " />"
        return format_html(html, flatatt(self.attrs))


if __name__ == "__main__":
    zw = ZenWidget("div", "", "test", {"class": "test", "width": "100%"})
    print zw.render()