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


class NavUl(ZenWidget):
    def __init__(self, css_classes):
        super(self.__class__, self).__init__("ul", {"class": css_classes})
        if not css_classes:
            self.css_classes = "nav navbar-nav"
            self.attrs["class"] = css_classes
        else:
            self.css_classes = css_classes

    def end_html(self):
        return "</ul>"


class NavDiv(ZenWidget):
    def __init__(self, css_classes):
        super(self.__class__, self).__init__("div", {"class": css_classes})
        if not css_classes:
            self.css_classes = "navbar-custom-menu"
            self.attrs["class"] = css_classes
        else:
            self.css_classes = css_classes

    def extra_appending(self):
        return NavUl("nav navbar-nav")

    def end_html(self):
        return "</div>"


class Nav(ZenWidget):
    def __init__(self,
                 css_classes="navbar navbar-static-top",
                 role="navigation",
                 id=None):
        super(self.__class__, self).__init__("nav", {"class": css_classes, "role": role}, id)
        if not css_classes:
            self.css_classes = "navbar navbar-static-top"
            self.attrs["class"] = css_classes

    def extra_appending(self):
        return NavDiv("navbar-custom-menu")


if __name__ == "__main__":
    nav = Nav()
    print(nav.render())
