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

class Icon(ZenWidget):
    def __init__(self, css_classes):
        super(self.__class__, self).__init__("i", {"class": css_classes})


class Span(ZenWidget):
    def __init__(self, css_classes, text):
        super(self.__class__, self).__init__("span", {"class": css_classes})
        self.append_text(text)


class Link(ZenWidget):
    def __init__(self, href="#",
                 css_classes=None, data_toggle=None,
                 role=None):
        attrs = {"href": href}
        if css_classes:
            attrs["class"] = css_classes
        if data_toggle:
            attrs["data-toggle"] = data_toggle
        if role:
            attrs["role"] = role
        super(self.__class__, self).__init__("a", attrs)

class DropdownMenu(ZenWidget):
    def __init__(self):
        super(self.__class__, self).__init__("ul", {"class": "dropdown-menu"})
        self.header = None
        self.footer = None
        self.menu_items = []

    def set_header(self, msg, link_href=None):
        self.header = ZenWidget("li", {"class": "header"})
        if link_href:
            link = Link(link_href)
            link.append_text(msg)
            self.append_widget(link)
        else:
            self.header.append_text(msg)

    def set_footer(self, msg, link_href=None):
        self.header = ZenWidget("li", {"class": "footer"})
        if link_href:
            link = Link(link_href)
            link.append_text(msg)
            self.append_widget(link)
        else:
            self.header.append_text(msg)

    def append_menuitem(self, item):
        self.menu_items.append(item)

    def render(self):
        self.sub_widgets = []
        if self.header:
            self.append_widget(self.header)
        for item in self.menu_items:
            self.append_widget(item)
        if self.footer:
            self.append_widget(self.footer)
        return super(self.__class__, self).render()
