#! / Usr / bin / python env
# - * - coding: UTF-8 - * -
try:
	from urllib import quote_plus #python 2
except:
	pass

try:
	from urllib.parse import quote_plus #python 3
except: 
	pass

from django.template.loader import get_template
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Modulo, Submodulo, Carpeta, SubCarpeta, Template, Documento
from profiles.models import Profile

from activitys.forms import ActivityForm

from .forms import ModuloForm, CarpetaForm, SubCarpetaForm, DocumentoForm


from django.utils import timezone

from django.template import loader

from django.db.models import Count


import pytz




def calendar_activity(request):
	

	obj_modulos	=	Modulo.objects.all()


	all_events = Carpeta.objects.all()
	get_event_types = Carpeta.objects.only('user_asign')
	if request.GET:  
		event_arr = []
		if request.GET.get('user_asign') == "all":
			all_events = Carpeta.objects.filter()
		else:   
			all_events = Carpeta.objects.filter(user_asign__icontains=request.GET.get('user_asign'))


		for i in all_events:
				event_sub_arr = {}
				event_sub_arr['title'] = i.event_name
				start_date = date(i.fecha_inicio.date(), "%Y-%m-%d")
				end_date = date(i.fecha_termino.date(), "%Y-%m-%d")
				event_sub_arr['start'] = start_date
				event_sub_arr['end'] = end_date

				event_arr.append(event_sub_arr)
		return HttpResponse(json.dumps(event_arr))

		
	form = ActivityForm(request.POST or None)

	if form.is_valid():

		activity = form.save(commit=False)

		fecha_init = timezone.now()

		fecha_inicio_data =		request.POST['fecha_inicio']
		fecha_termino_data =	request.POST['fecha_termino']

		activity.fecha_inicio = fecha_inicio_data
		activity.fecha_termino = fecha_termino_data
		activity.user_create_id  = request.user.id
		

		activity.save()
		activity.id
		print(activity.id)

		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/calendario_actividades')
	context = {
		"form": form,
		"all_events" : all_events,
		"obj_modulos": obj_modulos,

	}
	return render(request, "calendar.html", context)





def modulo_detail(request, id_modulo):


	id_modulo = id_modulo
	
	obj_get = Modulo.objects.get(id=id_modulo)

	form = ActivityForm(request.POST or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		print(obj_get.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/modulo/%s/' % id_modulo)


	context = {	
		"form": form,
		"obj_get" : obj_get,

	}
	return render(request, "modulo_detalle.html", context)



def submodulo_detail(request, id_modulo, id_submodulo):


	id_modulo = id_modulo

	id_submodulo = id_submodulo	
	
	obj_get = Submodulo.objects.get(id=id_submodulo)

	obj_modulo = Modulo.objects.get(id=id_modulo)

	obj_carpeta = Carpeta.objects.get(id=1)

	form = SubCarpetaForm(request.POST or None, instance=obj_carpeta)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		print(obj_get.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/submodulo/%s/' % id_submodulo)


	context = {	
		"form": form,
		"obj_get" : obj_get,
		"obj_modulo": obj_modulo,

	}
	if obj_get.id == 3:
		return render(request, "proceso.html", context)	
	if obj_get.id == 18:
		return render(request, "proceso.html", context)
	if obj_get.id == 19:
		return render(request, "proceso.html", context)
	if obj_get.id == 20:
		return render(request, "proceso.html", context)
	if obj_get.id == 21:
		return render(request, "proceso.html", context)
	if obj_get.id == 22:
		return render(request, "proceso.html", context)
	else:
		return render(request, "submodulo.html", context)	


def subcarpeta_edit(request, id_subcarpeta):

	obj_get = SubCarpeta.objects.get(id=id_subcarpeta)


	form = SubCarpetaForm(request.POST or None, instance=obj_get)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/')

	context = {	

		"obj_get" : obj_get,
		"form"		: form,
	}
	return render(request, "subcarpeta_edit.html", context)


def carpeta_detail(request, id_modulo, id_submodulo, id_carpeta):

	id_modulo = id_modulo

	id_submodulo = id_submodulo

	id_carpeta = id_carpeta	

	obj_modulo = Modulo.objects.get(id=id_modulo)

	obj_sub		= Submodulo.objects.get(id=id_submodulo)

	obj_get	=	Carpeta.objects.get(id=id_carpeta)


	obj_template	= Template.objects.all()




	form = ActivityForm(request.POST or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		print(obj_get.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/modulo/%s/' % id_modulo)

	context = {	

		"obj_get" : obj_get,
		"form"  : form,
		"obj_modulo": obj_modulo,
		"obj_sub":	obj_sub,
		"obj_template" : obj_template,

	}
	return render(request, "carpeta_detail.html", context)


def proceso_detail(request, id_modulo, id_submodulo, id_carpeta):

	id_modulo = id_modulo

	id_submodulo = id_submodulo

	id_carpeta = id_carpeta	

	obj_modulo = Modulo.objects.get(id=id_modulo)

	obj_sub		= Submodulo.objects.get(id=id_submodulo)

	obj_get	=	SubCarpeta.objects.get(id=id_carpeta)

	obj_template	= Template.objects.all()


	form = ActivityForm(request.POST or None, instance=obj_get)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		print(obj_get.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/modulo/%s/' % id_modulo)

	context = {	

		"obj_get" : obj_get,
		"form"  : form,
		"obj_modulo": obj_modulo,
		"obj_sub":	obj_sub,
		"obj_template": obj_template

	}
	return render(request, "carpeta_detail.html", context)

def subcarpeta_detail(request, id_modulo, id_submodulo, id_carpeta, id_subcarpeta):

	id_modulo = id_modulo

	id_submodulo = id_submodulo

	id_carpeta = id_carpeta	

	id_subcarpeta	= id_subcarpeta

	obj_modulo = Modulo.objects.get(id=id_modulo)

	obj_sub		= Submodulo.objects.get(id=id_submodulo)

	obj_get	=	Carpeta.objects.get(id=id_carpeta)

	obj_subcarp = SubCarpeta.objects.get(id=id_subcarpeta)


	form = ActivityForm(request.POST or None, instance=obj_get)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()	
		print(obj_get.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/modulo/%s/' % id_modulo)

	context = {	

		"obj_get" : obj_get,
		"form"  : form,
		"obj_modulo": obj_modulo,
		"obj_sub":	obj_sub,
		"obj_subcarp": obj_subcarp,

	}
	return render(request, "carpeta_detail.html", context)


def documento_select(request, id_modulo,id_submodulo, id_carpeta, id_doc): 

	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get1	=	SubCarpeta.objects.get(id=id_carpeta) 

	obj_template1 = Template.objects.get(id=id_doc)

	obj_get	=	Documento.objects.filter(template=obj_template1).order_by('-id')[:1]
	obj_template 		= Documento.objects.get(id=obj_get)
	date = timezone.now()

	form 	=	DocumentoForm(request.POST or None, instance=obj_template)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.fecha = date
		instance.save()
		new_instance = Documento(template=instance.template, user1=instance.user1, fecha=instance.fecha, titulo=instance.titulo, duracion=instance.duracion, descripcion=instance.descripcion, subtitulo1=instance.subtitulo1, subtitulo2=instance.subtitulo2, user2=instance.user2)
		new_instance.save()

		print(instance.id)
		print(new_instance.id)


	

	context = {	

		"obj_template" : obj_template,
		"obj_template1":	obj_template1,
		"form"		:	form,
		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get1": obj_get1,


	}	
	return render(request, "documento.html", context)




def select_users(request, id_modulo, id_submodulo, id_carpeta, id_docu, id_doc):
	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get1	=	SubCarpeta.objects.get(id=id_carpeta) 

	obj_get	=	Documento.objects.get(id=id_docu)

	obj_template = Template.objects.get(id=id_doc)


	context = {

		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get": obj_get,
		"obj_get1": obj_get1,
		"obj_template": obj_template,

	}
	return render(request, "table_asist.html", context)


def select_users2(request, id_modulo, id_submodulo, id_carpeta):
	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get	=	Carpeta.objects.get(id=id_carpeta)
	obj_profiles = Profile.objects.all()

	context = {
		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get": obj_get,
		"obj_profiles": obj_profiles,
	}
	return render(request, "table_asist2.html", context)



def huellero(request, id_modulo,id_submodulo, id_carpeta, id_docu, id_doc):

	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get1	=	SubCarpeta.objects.get(id=id_carpeta) 

	obj_get	=	Template.objects.get(id=id_doc)
	obj_docu1 		= Documento.objects.get(id=id_docu)

	context = {	

		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get1": obj_get1,
		"obj_docu1"	: obj_docu1,
		"obj_get": obj_get,

	}
	return render(request, "huella.html", context)



def firmas_asist(request, id_modulo,id_submodulo, id_carpeta, id_docu, id_doc):

	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get1	=	SubCarpeta.objects.get(id=id_carpeta) 

	obj_get	=	Template.objects.get(id=id_doc)

	date 	= timezone.now()

	obj_docu1 		= Documento.objects.get(id=id_docu)

	context = {	

		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get1": obj_get1,
		"obj_docu1"	: obj_docu1,
		"date" 	: date,
		"obj_get": obj_get,

	}	

	return render(request, "firmas_asist.html", context)


def docu_generate(request, id_modulo,id_submodulo, id_carpeta, id_doc, id_docu):
	date 	= timezone.now()

	obj_modulo = Modulo.objects.get(id=id_modulo)
	obj_sub		= Submodulo.objects.get(id=id_submodulo)
	obj_get1	=	SubCarpeta.objects.get(id=id_carpeta) 

	obj_get	=	Template.objects.get(id=id_doc)
	obj_docu1 		= Documento.objects.get(id=id_docu)

	context = {	

		"obj_modulo": obj_modulo,
		"obj_sub": obj_sub,
		"obj_get1": obj_get1,
		"obj_get" : obj_get,
		"obj_docu1"	: obj_docu1,
		"date" 	: date

	}	
	return render(request, "docu_select.html", context)


from django.views.generic import View
from blog.util import render_pdf

class PDFPrueba(View):

	def get(self, request, nombre, id_docu, *args, **kwargs):

		obj_get1	=	Template.objects.filter(nombre=nombre)
		obj_get 	= 	Template.objects.get(id=obj_get1)

		obj_docu1 	= 	Documento.objects.get(id=id_docu)
		date 	= timezone.now()

		context = {	
			"title1"		: 	obj_get.nombre,
			"titulo" 		:	obj_docu1.titulo,
			"subtitulo1" 	:	obj_docu1.subtitulo1,
			"subtitulo2" 	:	obj_docu1.subtitulo2,
			"content"		:	obj_docu1.get_markdown,
			"user1_name"	: 	obj_docu1.user1.user.first_name,
			"user1_last"	: 	obj_docu1.user1.user.last_name,
			"rut"			:	obj_docu1.user1.rut,
			"cargo"			:	obj_docu1.user1.cargo,
			"fecha"			:	date,
			"depto"			:	obj_docu1.depto,
			"duracion"		:	obj_docu1.duracion,
			"user2_name"	:	obj_docu1.user2.user.first_name,
			"user2_last"	:	obj_docu1.user2.user.last_name,
			"cargo2"		:	obj_docu1.user2.cargo,

		}	
		pdf = render_pdf("prueba.html", {"context": context})
		return HttpResponse(pdf, content_type="application/pdf", )





