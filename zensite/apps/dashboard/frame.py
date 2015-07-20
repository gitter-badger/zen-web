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

from zensite.widgets.nav import create_navbar
from zensite.widgets.sidebar import create_sidebar

NAVBAR = "navbar"
SIDEBAR = "sidebar"


class Frame:
    _navbar = None
    _sidebar = None
    _content = None

    def __init__(self, components=[NAVBAR, SIDEBAR]):
        if NAVBAR in components:
            self._navbar = navbar()
        if SIDEBAR in components:
            self._sidebar = create_sidebar()
