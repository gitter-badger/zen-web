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
from link import Link, Icon, Span


def nav_toggle_button():
    btn = Link("#", "sidebar-toggle", "offcanvas", "button")
    btn.append_widget(Span("sr-only", "Toggle navigation"))
    return btn

def nav_dd_icon(icon_class="fa fa-envelope-o", label_class="label label-success", label_text=""):
    link = Link(href="#", css_classes="dropdown-toggle", data_toggle="dropdown")
    icon = Icon(icon_class)
    span = Span(label_class, label_text)
    icon.append_widget(span)
    link.append_widget(icon)
    return link


def nav_dd_envelope_icon(label_text):
    return nav_dd_icon("fa fa-envelope-o", "label label-success", label_text)


def nav_dd_notification_icon(label_text):
    return nav_dd_icon("fa fa-bell-o", "label label-warning", label_text)


def nav_dd_task_icon(label_text):
    return nav_dd_icon("fa fa-flag-o", "label label-danger", label_text)


class NavDropdownMenu(ZenWidget):
    def __init__(self, menu_type, icon):
        super(self.__class__, self).__init__("li", {"class": "dropdown %s" % menu_type})
        self.icon = icon
        self.append_widget(self.icon)
        self.dropdown = None

    def set_dropdown_menu(self, dropdown):
        self.dropdown = dropdown

    def render(self):
        if self.dropdown:
            if not self.dropdown in self.sub_widgets():
                self.append_widget(self.dropdown)
        return super(self.__class__, self).render()


class NavUl(ZenWidget):
    def __init__(self, css_classes="nav navbar-nav"):
        super(self.__class__, self).__init__("ul", {"class": css_classes})
        if not css_classes:
            self.css_classes = "nav navbar-nav"
            self.attrs["class"] = css_classes
        else:
            self.css_classes = css_classes



class NavDiv(ZenWidget):
    def __init__(self, css_classes="navbar-custom-menu"):
        super(self.__class__, self).__init__("div", {"class": css_classes})
        if not css_classes:
            self.css_classes = "navbar-custom-menu"
            self.attrs["class"] = css_classes
        else:
            self.css_classes = css_classes
        self.nav_ul = NavUl("nav navbar-nav")
        self.append_widget(self.nav_ul)

    def append_nav_widget(self, widget):
        self.nav_ul.append_widget(widget)


class Nav(ZenWidget):
    def __init__(self, toggle_button=True,
                 css_classes="navbar navbar-static-top",
                 role="navigation",
                 id=None):
        super(self.__class__, self).__init__("nav",
                                             {"class": css_classes,
                                              "role": role},
                                             id)
        if not css_classes:
            self.css_classes = "navbar navbar-static-top"
            self.attrs["class"] = css_classes
        self.toggle_button = toggle_button
        if self.toggle_button:
            self.append_widget(nav_toggle_button())
        self.nav_div = NavDiv("navbar-custom-menu")
        self.append_widget(self.nav_div)

    def append_nav_widget(self, widget):
        self.nav_div.append_widget(widget)


dev create_navbar():
    nav = Nav()
    # todo
    return nav


if __name__ == "__main__":
    nav = Nav()
    nav.append_nav_widget(NavDropdownMenu("messages-menu", nav_dd_envelope_icon("1")))
    nav.append_nav_widget(NavDropdownMenu("notifications-menu", nav_dd_notification_icon("2")))
    nav.append_nav_widget(NavDropdownMenu("tasks-menu", nav_dd_task_icon("3")))
    print(nav.render())
