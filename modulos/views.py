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


from .models import Modulo, Submodulo, Carpeta, SubCarpeta
from profiles.models import Profile

from activitys.forms import ActivityForm

from .forms import ModuloForm, CarpetaForm, SubCarpetaForm


from django.utils import timezone


import pytz









def activity_create(request):
	
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404


	all_events = Activity.objects.all()
	get_event_types = Activity.objects.only('user_asign')
	if request.GET:  
		event_arr = []
		if request.GET.get('user_asign') == "all":
			all_events = Activity.objects.filter()
		else:   
			all_events = Activity.objects.filter(user_asign__icontains=request.GET.get('user_asign'))


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
		"fecha_init" : fecha_init
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

	form = CarpetaForm(request.POST or None, instance=obj_carpeta)

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

	obj_get1	=	Carpeta.objects.get(id=id_carpeta)

	obj_get	=	SubCarpeta.objects.get(id=id_carpeta) 




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
		"obj_get1": obj_get1,
		"form"  : form,
		"obj_modulo": obj_modulo,
		"obj_sub":	obj_sub,

	}
	return render(request, "carpeta_detail.html", context)


def proceso_detail(request, id_modulo, id_submodulo, id_carpeta):

	id_modulo = id_modulo

	id_submodulo = id_submodulo

	id_carpeta = id_carpeta	

	obj_modulo = Modulo.objects.get(id=id_modulo)

	obj_sub		= Submodulo.objects.get(id=id_submodulo)

	obj_get	=	Carpeta.objects.get(id=id_carpeta)


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

	}
	return render(request, "subproceso.html", context)

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
