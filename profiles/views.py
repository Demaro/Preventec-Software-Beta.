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

from profiles.forms import ProfileForm, ProfileDocForm, ProfileDatosForm, ProfileObreroForm, ProfileDatosObreroForm, ProfileDocObreroForm
from profiles.models import Profile, Perfil_Obrero, Cargo
from posts.models import Post

from django.utils import timezone

from accounts.views import (login_view, register_view, logout_view) 

from accounts.forms import  UserRegisterForm, UserNamesForm

from modulos.forms import ModuloForm




from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)

User = get_user_model()

from modulos.models import Modulo, Submodulo


def casa(request):

	return render(request, "home.html")

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Bienvenido')
	else:
		return HttpResponseRedirect('/inicio')


def detail_actividad(request):
	return render(request, "detail_actividad.html")

def principal(request):
	obj_profiles = Profile.objects.all()
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')

	context = {
	"obj_profiles": obj_profiles,
	}	
	return render(request, "index.html", context)

def profiles_contacts(request):

	object_list = Profile.objects.filter(user__is_staff="True")
	context	=	{
	"object_list": object_list,
	}
	return render(request, "contacts.html", context)

def actividades(request):
	return render(request, "activitys.html")


"""

	query = request.GET.get("modules")
	if query:
		queryset_list = queryset_list.filter(
				Q(id__icontains=query)|
				Q(porcent__icontains=query)|
				Q(estado__icontains=query) 
				).distinct()
	paginator = Paginator(queryset_list, 6) # Show 25 contacts per page
	page_request_var = "pagina"
	pagina = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(pagina)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

"""


def modules(request):

	queryset_list = Modulo.objects.all().order_by("id")


	form 		= ModuloForm(request.POST)


	context = {
		#"queryset_list": queryset, 
		#"page_request_var": page_request_var,
		"queryset_list" : queryset_list,
		"form": form
	}	
	return render(request, "modules_form.html", context)

def seis(request):
	return render(request, "maps.html")

def siete(request):
	return render(request, "notifications.html")



#Creacion del perfil staff
def crear_perfil_staff(request, id_user):
	if request.user.is_authenticated():
		instance1	=	id_user
		obj 	= User.objects.get(id=id_user)
		form2 = ProfileForm(request.POST or None)
		form = UserNamesForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance1 = form.save(commit=False)
			instance1.save()
		
		if form2.is_valid():
			instance = form2.save(commit=False)
			instance.user = obj
			instance.ultimateupdate = timezone.now()
			instance.inicio_cargo = timezone.now()
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/perfil_datos_staff/%s' % instance.id )

	context = {
		"obj":obj,
		"form": form,
		"form2": form2,
	}
	return render(request, "create_profile.html", context)


def perfil_datos_staff(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Profile.objects.get(id=id_profile)
		form 	= ProfileDatosForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/cargar_documentos/%s' % instance.id )
	context = {
		"obj": obj,
		"form": form,
	}
	return render(request, "perfil_datos_staff.html", context)



def perfil_datos_staff2(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Profile.objects.get(id=id_profile)
		form 	= ProfileDatosForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/cargar_documentos_edit/%s' % instance.id )
	context = {
		"obj": obj,
		"form": form,
		"instance": instance
	}
	return render(request, "perfil_datos_staff.html", context)


def carga_docu(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Profile.objects.get(id=id_profile)
		form 	= ProfileDocForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/gestion_usuarios')
	context = {
		"obj": obj,
		"form": form,
	}
	return render(request, "cargar_docu.html", context)


def carga_docu2(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Profile.objects.get(id=id_profile)
		form 	= ProfileDocForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/perfil-detalle/%s' % instance.id )
	context = {
		"obj": obj,
		"form": form,
		"instance":	instance

	}
	return render(request, "cargar_docu.html", context)


#Creacion del Perfil Obrero

def crear_perfil_obrero(request):
	if request.user.is_authenticated():
		form = ProfileObreroForm(request.POST or None)
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.ultimateupdate = timezone.now()
			instance.inicio_cargo = timezone.now()
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/perfil_datos_obrero/%s' % instance.id )

	context = {
		"form": form,
	}
	return render(request, "create_profile_obrero.html", context)


def perfil_datos_obrero(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Perfil_Obrero.objects.get(id=id_profile)
		form 	= ProfileDatosObreroForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/cargar_documentos_obrero/%s' % instance.id )
	context = {
		"obj": obj,
		"form": form,
	}
	return render(request, "perfil_datos_obrero.html", context)


def carga_docu_obrero(request, id_profile):
	if request.user.is_authenticated():
		instance = id_profile
		obj 	= Perfil_Obrero.objects.get(id=id_profile)
		form 	= ProfileDocObreroForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print(instance.id)
			return HttpResponseRedirect('/gestion_usuarios')
	context = {
		"obj": obj,
		"form": form,
	}
	return render(request, "cargar_docu_obrero.html", context)

def profile_list(request):
	profiles_obj = Profile.objects.all().order_by("-ultimateupdate")
	user_list = User.objects.all()


	context = {
		"profiles_obj": profiles_obj, 
		"user_list": user_list

	}
	return render(request, "profile_list.html", context)




def profile_detail(request, id_profile):
	object_list = Profile.objects.filter(id=id_profile)

	context = {
		"object_list": object_list,
		
	}
	return render(request, "profile_detail.html", context)


def profile_detail_obrero(request, id_profile):
	objects_list = Perfil_Obrero.objects.filter(id=id_profile)
	context = {
		"objects_list": objects_list,

	}
	return render(request, "profile_detail_obrero.html", context)






def profile_update(request, id_profile):
	instance = Profile.objects.get(id=id_profile)
	id_user = instance.user.id
	obj 	= User.objects.get(id=id_user)
	if request.user.is_superuser:

		form = UserNamesForm(request.POST or None, instance=obj)
		if form.is_valid():
			instance1 = form.save(commit=False)
			instance1.save()


		form2 = ProfileForm(request.POST or None,  instance=instance)
		if form2.is_valid():
			instance = form2.save(commit=False)
			instance.ultimateupdate = timezone.now()
			instance.save()
			messages.success(request, "<a href='#'>Item</a> Modificado!", extra_tags='html_safe')
			return HttpResponseRedirect('/perfil_datos_staff_edit/%s/' % id_profile)

		context = {
			"instance": instance,
			"form2":form2,
			"form": form,
		}
		return render(request, "create_profile.html", context)
	else:
		raise Http404



def profile_update_obrero(request, id_profile):
	instance = Perfil_Obrero.objects.get(id=id_profile)
	form = ProfileObreroForm(request.POST or None,  instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.ultimateupdate = timezone.now()
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Modificado!", extra_tags='html_safe')
		return HttpResponseRedirect('/perfil_datos_obrero/%s/' % id_profile)

	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, "create_profile_obrero.html", context)



def profile_delete(request, id_profile):
	instance = Profile.objects.get(id=id_profile)
	if request.user.is_superuser:
		instance.delete()
		messages.success(request, "Eliminado con exito")
		return redirect("profile:list")
	else:
		raise Http404