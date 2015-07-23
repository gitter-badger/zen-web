#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#

from django.template.loader import get_template
from django import template
from django.template import Context
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render_to_response

from frame import Frame
from zensite.widgets.misc import render_logo


@require_http_methods(["GET"])
def display_dashboard(request):
	if request.user.is_authenticated:
		frame = Frame()
		logo_html = render_logo("http://esse.io", "Z", "en", "Zen", "esse.io")

		context = Context({
			'page_title': 'Zen | Dashboard',
			"zen_frame": frame,
			"logo_html": logo_html,
			})

		#header_t = get_template('header.html')
		#header_html = header_t.render(context)

		#t = get_template('dashboard.html')
		#html = t.render(context)

		#footer_t = get_template('footer.html')
		#footer_html = footer_t.render(context)
		#return HttpResponse(header_html + html + footer_html)
		return render_to_response('frame.html', context,
								  content_type="text/html")
	else:
		return render_to_response('/login', {},
        						  content_type="text/html")

