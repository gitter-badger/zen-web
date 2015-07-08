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

    def __init__(self, element_name, attrs=None, id=None, name=None):
        if id:
            self.id = id
        if attrs:
            self.attrs = attrs.copy()
        else:
            self.attrs = {}
        self.element_name = element_name
        if name:
            self.name = name

    def append_text(self, text):
        self.text = text

    def append_widget(self, widget):
        self.sub_widgets.append(widget)

    def render(self):
        if self.name:
            self.attrs['name'] = self.name
        if self.id:
            self.attrs['id'] = self.id
        final_attrs = self.build_attrs(self.attrs)
        html = "<{}".format(self.element_name)
        html = html + "{}"
        if self.text:
            html = html + " >{}".format(self.text) + "</{}>".format(self.element_name)
        elif self.sub_widgets:
            extra_appending = self.extra_appending()
            if extra_appending:
                html += extra_appending.render()
            for widget in self.sub_widgets:
                html += widget.render()
            if extra_appending:
                html += extra_appending.end_html()
            html = html + "</{}>".format(self.element_name)
        else:
            html = html + " />"
        return format_html(html, flatatt(self.attrs))

    def end_html():
        return ""
`
    def extra_appenging(self):
        return None

if __name__ == "__main__":
    zw = ZenWidget("div", {"class": "test", "width": "100%"}, "testid", "test")
    print zw.render()