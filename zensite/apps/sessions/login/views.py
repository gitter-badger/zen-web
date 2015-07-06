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


def login(request):
	context = Context({
		'page_title': 'Zen | Login',
		})
	header_t = get_template('header.html')
	header_html = header_t.render(context)

	t = get_template('login.html')
	html = t.render(context)

	footer_t = get_template('footer.html')
	footer_html = footer_t.render(context)
	return HttpResponse(header_html + html + footer_html)


def login_submit(request):
	return HttpResponse('')
