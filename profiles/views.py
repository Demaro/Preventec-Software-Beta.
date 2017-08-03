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


def profile_create(request, id_user):
	print(id_user)
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404	
	
	form = ProfileForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		id_instance = instance.id 
		
		instance.ultimateupdate = timezone.now()
		instance.user_id = id_user
		instance.save()
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/')
	context = {
		"form": form,
	}
	return render(request, "perfil_form.html", context)




def profile_list(request):
	today = timezone.now().date()
	if not request.user.is_authenticated():
			queryset_list = Profile.objects.all().order_by("-ultimateupdate")
	if request.user.is_active:
			queryset_list = Profile.objects.filter(user=request.user).order_by("-ultimateupdate")
	if request.user.is_staff or request.user.is_superuser:
			queryset_list = Profile.objects.all().order_by("-ultimateupdate")
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(rut__icontains=query)|
				Q(cargo__icontains=query)|
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "profile_list.html", context)


"""

def profile_detail(request, id_perfil):
		if not request.user.is_authenticated() or request.user.is_active:
			raise Http404
		if request.user.is_superuser:
			detail = Profile.objects.get(id=id_perfil)

		return render(request, "profile_list.html")

"""