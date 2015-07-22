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


class LinkItem(ZenWidget):
    def __init__(self, li_class):
        super(self.__class__, self).__init__("li", {"class": li_class})

    def set_href(self, href="#", css_classes=None, data_toggle=None,
                 role=None):
        self.link = Link(href, css_classes, data_toggle, role)

    def set_icon(self, css_classes=""):
        self.icon = Icon(css_classes)

    def set_span(self, css_classes="", text=""):
        self.span = Span(css_classes, text)

    def render(self):
        if self.link:
            self.append_widget(self.link)
            if self.icon:
                self.link.append_widget(self.icon)
                if self.span:
                    self.icon.append_widget(self.span)
        return super(self.__class__, self).render()


class TreeViewMenu(ZenWidget):
    def __init__(self, css_classes="treeview-menu"):
        super(self.__class__, self).__init__("ul", {"class": css_classes})
        self.link_items = []

    def append_linkitem(self, linkitem):
        self.link_items.append(linkitem)

    def render(self):
        for item in self.link_items:
            self.append_widget(item)
        return super(self.__class__, self).render()


class TreeView(ZenWidget):
    def __init__(self, css_classes="treeview"):
        super(self.__class__, self).__init__("li", {"class": css_classes})
        self.title = None
        self.treeview_menu = None

    def set_title(self, link):
        self.title = link

    def set_treeview_menu(self, menu):
        self.treeview_menu = menu

    def render(self):
        if self.title:
            self.append_widget(self.title)
        if self.treeview_menu:
            self.append_widget(self.treeview_menu)
        return super(self.__class__, self).render()


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
