# encoding: utf-8
#! / Usr / bin / python env
# - * - coding: UTF-8 - * -

from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_pdf(url_template, contexto={}):

	template = get_template(url_template)
	html	= template.render(contexto)
	result	= BytesIO()
	pdf =	pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type="application/pdf")
	return None