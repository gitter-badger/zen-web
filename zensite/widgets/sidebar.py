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
from misc import Image
from link import Link, Icon, Span


class SideBar(ZenWidget):
    def __init__(self, user_info=None):
        """
            user_info: {"username": "xxxx", "userimg": "xxxx", "userstatus":"online"}
        """
        super(self.__class__, self).__init__("aside",
                                             {"class": "main-sidebar"})
        self.section = ZenWidget("section", {"class": "sidebar"})
        self.user_info = user_info
        if not self.user_info:
            self.user_info = {}
        self.sidebar_menu = ZenWidget("ul", {"class": "sidebar-menu"})
        self.menu_items = []

    def update_user_info(self, user_info):
        self.user_info.merge(user_info)

    def _compose_user_panel(self):
        userpanel = ZenWidget("div", {"class": "user-panel"})
        userimagediv = ZenWidget("div", {"class": "pull-left image"})
        userpanel.append_widget(userimagediv)
        userimg = Image(self.user_info["src"], self.user_info["css_classes"], self.user_info["alt"])
        userimagediv.append_widget(userimg)

        usernamediv = ZenWidget("div", {"class": "pull-left info"})
        p = ZenWidget("p")
        p.append_text(self.user_info["username"])
        userimagediv.append_widget(p)
        userstatus = Link("#")
        userstatusicon = Icon("fa fa-circle text-success")
        userstatusicon.append_text(self.user_info["userstatus"])
        userstatus.append_widget(userstatusicon)
        userimagediv.append_widget(userstatus)
        userpanel.append_widget(userstatus)

        return userpanel

    def append_menuitem(self, item):
        self.menu_items.append(item)

    def render(self):
        if self.user_info:
            self.section.append_widget(self._compose_user_panel())
        if self.menu_items:
            for i in self.menu_items:
                self.sidebar_menu.append_widget(i)
        self.append_widget(self.section)
        self.section.append_widget(self.sidebar_menu)
        return super(self.__class__, self).render()


def create_sidebar(user_info=None):
    sidebar = SideBar(user_info)
    return sidebar
