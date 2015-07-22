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


class Image(ZenWidget):
	def __init__(self, src, css_classes, alt=""):
		super(self.__class__, self).__init__("img",
                                         {"class": css_classes,
                                          "src": src,
                                          "alt": alt})


def render_logo(href, mini_logo_highlight, mini_logo,
	            lg_logo_highlight, lg_logo):
	logo_html = """
    <!-- Logo -->
    <a href='{href}' class='logo'>
      <!-- mini logo for sidebar mini 50x50 pixels -->
      <span class='logo-mini'><b>{mini_logo_highlight}</b>{mini_logo}</span>
      <!-- logo for regular state and mobile devices -->
      <span class='logo-lg'><b>{lg_logo_highlight}</b>&nbsp;{lg_logo}</span>
    </a>
    """

	return logo_html.format(
    	href=href,
    	mini_logo_highlight=mini_logo_highlight,
    	mini_logo=mini_logo,
    	lg_logo_highlight=lg_logo_highlight,
    	lg_logo=lg_logo
    	)


if __name__ == "__main__":
    html = render_logo("http://esse.io", "Z", "en", "Zen", "esse.io")
    print html