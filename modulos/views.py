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


from .models import Modulo
from profiles.models import Profile

from activitys.forms import ActivityForm


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
	
	obj_get = Modulo.objects.filter(id=id_modulo)[0]

	form = ActivityForm(request.POST)



	if form.is_valid():

		activity = form.save(commit=False)

		fecha_inicio_data =		request.POST['fecha_inicio']
		fecha_termino_data =	request.POST['fecha_termino']
		carpetas =				request.POST.getlist('table_records')


		activity.fecha_inicio = fecha_inicio_data
		activity.fecha_termino = fecha_termino_data
		user = request.user.id
		activity.user_create_id  = user
		for c in carpetas:
			activity.carpeta 		=	c
			
		activity.save()
		activity.id
		print(activity.id)
		print(activity.user_asign)
		
		print(activity.carpeta)


		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/calendario_actividades')
	context = {	

		"obj_get" : obj_get,
		"form"  : form,

		}
	return render(request, "modulo_detalle.html", context)
