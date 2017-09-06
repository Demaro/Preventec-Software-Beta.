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

from accounts.views import (login_view, register_view, logout_view) 

from accounts.forms import  UserRegisterForm

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)

User = get_user_model()

from modules.models import Modulo, Submodulo


def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
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
	return render(request, "contacts.html")

def actividades(request):
	return render(request, "activitys.html")

def modules(request):
	obj_all = Modulo.objects.get(id=1)
	obj_sub = Submodulo.objects.filter(modulo_id=1).order_by("nombre")

	obj_all2 = Modulo.objects.get(id=2)
	obj_sub2 = Submodulo.objects.filter(modulo_id=2).order_by("nombre")

	obj_all3 = Modulo.objects.get(id=3)
	obj_sub3 = Submodulo.objects.filter(modulo_id=3).order_by("nombre")

	obj_all4 = Modulo.objects.get(id=4)
	obj_sub4 = Submodulo.objects.filter(modulo_id=4).order_by("nombre")

	obj_all5 = Modulo.objects.get(id=5)
	obj_sub5 = Submodulo.objects.filter(modulo_id=5).order_by("nombre")

	obj_all6 = Modulo.objects.get(id=6)
	obj_sub6 = Submodulo.objects.filter(modulo_id=6).order_by("nombre")

	obj_all7 = Modulo.objects.get(id=7)
	obj_sub7 = Submodulo.objects.filter(modulo_id=7).order_by("nombre")

	obj_all8 = Modulo.objects.get(id=8)
	obj_sub8 = Submodulo.objects.filter(modulo_id=8).order_by("nombre")

	obj_all9 = Modulo.objects.get(id=9)
	obj_sub9 = Submodulo.objects.filter(modulo_id=9).order_by("nombre")

	obj_all10 = Modulo.objects.get(id=10)
	obj_sub10 = Submodulo.objects.filter(modulo_id=10).order_by("nombre")

	obj_all11 = Modulo.objects.get(id=11)
	obj_sub11 = Submodulo.objects.filter(modulo_id=11).order_by("nombre")

	obj_all12 = Modulo.objects.get(id=12)
	obj_sub12 = Submodulo.objects.filter(modulo_id=12).order_by("nombre")




	context = {
	"obj_all": obj_all,
	"obj_sub": obj_sub,

	"obj_all2": obj_all2,
	"obj_sub2": obj_sub2,

	"obj_all3": obj_all3,
	"obj_sub3": obj_sub3,

	"obj_all4": obj_all4,
	"obj_sub4": obj_sub4,

	"obj_all5": obj_all5,
	"obj_sub5": obj_sub5,

	"obj_all6": obj_all6,
	"obj_sub6": obj_sub6,

	"obj_all7": obj_all7,
	"obj_sub7": obj_sub7,

	"obj_all8": obj_all8,
	"obj_sub8": obj_sub8,

	"obj_all9": obj_all9,
	"obj_sub9": obj_sub9,

	"obj_all10": obj_all10,
	"obj_sub10": obj_sub10,

	"obj_all11": obj_all11,
	"obj_sub11": obj_sub11,

	"obj_all12": obj_all12,
	"obj_sub12": obj_sub12

	}	
	return render(request, "modules_form.html", context)

def seis(request):
	return render(request, "maps.html")

def siete(request):
	return render(request, "notifications.html")




def profile_create(request, id_user):
	if request.user.is_authenticated():
		form = ProfileForm(request.POST or None)
		username = User.objects.get(id=id_user)
	if form.is_valid():

		rut_data = form.cleaned_data.get("rut")
		birthdate_data = form.cleaned_data.get("birthdate")
		avatar_data = form.cleaned_data.get("avatar")
		cargo_data = form.cleaned_data.get("cargo")
		contrato_data = form.cleaned_data.get("contrato")
		legales_asoc_data = form.cleaned_data.get("legales_asoc")

		new_profile = Profile(user_id=id_user, rut=rut_data, birthdate=birthdate_data, avatar=avatar_data, cargo=cargo_data, contrato=contrato_data, legales_asoc=legales_asoc_data,  ultimateupdate = timezone.now(), inicio_cargo=timezone.now())

		new_profile.save()

		new_profile.id
		print(new_profile.id)
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/inicio')
	context = {
		"form": form,
		"id_user": id_user,
		"username": username,
	}
	return render(request, "profile_form.html", context)




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
	return render(request, "profile_detail.html", {"object_list": object_list})



def profile_update(request, id_profile):
	instance = Profile.objects.get(id=id_profile)
	if request.user.is_superuser:
		form2 = ProfileForm(request.POST or None,  instance=instance)
		if form2.is_valid():
			instance = form2.save(commit=False)
			instance.ultimateupdate = timezone.now()
			instance.save()
			messages.success(request, "<a href='#'>Item</a> Modificado!", extra_tags='html_safe')
			return HttpResponseRedirect('/perfil-detalle/%s/' % id_profile)

		context = {
			"instance": instance,
			"form2":form2,
		}
		return render(request, "user.html", context)
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