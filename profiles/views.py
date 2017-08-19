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

from profiles.forms import ProfileForm
from profiles.models import Profile
from posts.models import Post

from django.utils import timezone

from accounts.forms import  UserRegisterForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

User = get_user_model()


def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		return HttpResponseRedirect('/inicio')


def detail_actividad(request):
	return render(request, "detail_actividad.html")

def principal(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
		
	return render(request, "index.html")

def tres(request):
	return render(request, "table.html")

def actividades(request):
	return render(request, "actividades.html")

def cinco(request):
	return render(request, "icons.html")

def seis(request):
	return render(request, "maps.html")

def siete(request):
	return render(request, "notifications.html")



def profile_create(request, id_user):
	if request.user.is_authenticated():
			form = ProfileForm(request.POST or None)
	if form.is_valid():

		rut_data = form.cleaned_data.get("rut")
		birthdate_data = form.cleaned_data.get("birthdate")
		avatar_data = form.cleaned_data.get("avatar")
		cargo_data = form.cleaned_data.get("cargo")
		especialidad_data = form.cleaned_data.get("especialidad")
		contrato_data = form.cleaned_data.get("contrato")
		legales_asoc_data = form.cleaned_data.get("legales_asoc")

		new_profile = Profile(user_id=id_user, rut=rut_data, birthdate=birthdate_data, avatar=avatar_data, cargo=cargo_data, especialidad=especialidad_data, contrato=contrato_data, legales_asoc=legales_asoc_data, ultimateupdate = timezone.now(), inicio_cargo=timezone.now())

		new_profile.save()
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/profiles')
	context = {
		"form": form,
		"id_user": id_user,
	}
	return render(request, "profile_create.html", context)




def profile_list(request):
	queryset_list = Profile.objects.all().order_by("-ultimateupdate")
	form = UserRegisterForm(request.POST or None)
	today = timezone.now().date()
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		email = form.cleaned_data.get("email")
		nombre = form.cleaned_data.get("first_name")
		apellido = form.cleaned_data.get("last_name")
		new_user = User(username=username, password=password, email=email, first_name=nombre, last_name=apellido)
		new_user.save()
		#login(request, new_user)
		new_user.id
		print(new_user.id)
		return HttpResponseRedirect('crear_perfil/%s/' % new_user.id)


	context = {
		"queryset_list": queryset_list, 

	}
	return render(request, "user.html", context)




def profile_detail(request, id_profile):
	object_list = Profile.objects.filter(id=id_profile)
	return render(request, "profile_detail.html", {"object_list": object_list})



def profile_update(request, id_profile):
	instance = Profile.objects.get(id=id_profile)
	if request.user.is_superuser:
		form = ProfileForm(request.POST or None,  instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.ultimateupdate = timezone.now()
			instance.save()
			messages.success(request, "<a href='#'>Item</a> Modificado!", extra_tags='html_safe')
			return HttpResponseRedirect('/perfil-detalle/%s/' % id_profile)

		context = {
			"instance": instance,
			"form":form,
		}
		return render(request, "profile_create.html", context)
	else:
		raise Http404




def profile_delete(request, id_profile):
	instance = Profile.objects.get(id=id_profile)
	if request.user.is_superuser:
		instance.delete()
		messages.success(request, "Eliminado con exito")
		return redirect("profile:list")
	else:
		raise Http404