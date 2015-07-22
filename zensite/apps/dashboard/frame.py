#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response

from zensite.widgets.base import ZenWidget
from zensite.widgets.nav import create_navbar
from zensite.widgets.sidebar import create_sidebar
from zensite.widgets.content_wrapper import ContentWrapper


NAVBAR = "navbar"
SIDEBAR = "sidebar"


class Frame:
    _navbar = None
    _sidebar = None
    _content_wrapper = None

    def __init__(self, components=[NAVBAR, SIDEBAR]):
        if NAVBAR in components:
            self._navbar = navbar()
        if SIDEBAR in components:
            self._sidebar = create_sidebar()
        self._content_wrapper = ContentWrapper()

    def append_nav_widget(self, widget):
        if self._navbar:
            self._navbar.append_nav_widget(widget)

    def append_side_menu(self, item):
        if self._sidebar:
            self._sidebar.append_menuitem(item)


    def get_navbar(self):
        return self._navbar

    def get_sidebar(self):
        return self._sidebar

    def get_content_wrapper(self):
        return self._content_wrapper
