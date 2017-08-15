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

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post


from django.utils import timezone




def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.publish = timezone.now()
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_authenticated():
			raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	today = timezone.now().date()
	if not request.user.is_authenticated():
			queryset_list = Post.objects.all().order_by("-timestamp")
	if request.user.is_active:
			queryset_list = Post.objects.filter(user=request.user).order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
			queryset_list = Post.objects.all().order_by("-timestamp")
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
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
	return render(request, "index.html", context)





def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if request.user == instance.user:
		form = PostForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
			return HttpResponseRedirect(instance.get_absolute_url())

		context = {
			"title": instance.title,
			"instance": instance,
			"form":form,
		}
		return render(request, "post_form.html", context)
	else:
		raise Http404





def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	if request.user == instance.user:
		instance.delete()
		messages.success(request, "Eliminado con exito")
		return redirect("posts:list")
	else:
		raise Http404


def resume(request):
	myresume = {
  "basics": {
    "name": "David Martinez",
    "label": "Programador. Analista de sistemas.",
    "picture": "",
    "email": "demaromail@gmail.com",
    "phone": "+569 567 504 80",
    "website": "https://richardhendricks.com",
    "summary": "En el estudio autodidacta y profesional de informática y como programador dedicado junto al analis de sistema es donde me entrego totalmente por los proyectos a desarrollar, usar tecnologías de preferencia para dar soluciones optimas e ideales, con la pasión al crearlas, lenguajes de programación  como Python y con el framework de Django, desarrollando Apis, herramientas q me permitieron elaborar importantes aplicaciones que con pro-actividad y motivación se lograron implantar. Sistemas encargados de gestionar las bodegas de insumos entrantes y de salidas, administrable para especialidades del CAE, operativa en Hospital Regional Rancagua.  También otros proyectos personales por amor al arte de programar para profundizar mis conocimientos como Backend, donde destaco el consumo de Apis, formato Json, postgreSQL y Django Restful.",
    "location": {
      "address": "Torres del paine, 0446",
      "postalCode": "",
      "city": "Rancagua",
      "countryCode": "US",
      "region": "Libertador bernardo O'higgins "
    },
    "profiles": [
      {
        "network": "GitHub",
        "username": "Demaro",
        "url": "https://github.com/Demaro"
      },
      {
        "network": "StackOverFlow",
        "username": "demaro-create",
        "url": "https://stackoverflow.com/users/7672972/demaro-create"
      }
    ]
  },
  "work": [
    {
      "company": "HRR",
      "position": "Desarrollador/Analista",
      "website": "http://www.saludohiggins.cl/",
      "startDate": "2017-01-09",
      "endDate": "2017-04-25",
      "summary": "Departamento de desarrollo informático. Hospital regional Rancagua.",
      "highlights": [
        "Toma de requerimientos a funcionarios.",
        "Programación orientada a objeto, aplicación web, escalable.",
        "Optimizar código, funciones y capacitación de usuarios administrativos y encargados."
      ]
    }
  ],
  "volunteer": [
    {
      "organization": "HCMfront",
      "position": "Programador",
      "website": "https://www.hcmfront.com/",
      "startDate": "2017-03-10",
      "endDate": "2017-04-30",
      "summary": "Gestión web de Personas Inteligencia en RRHH, al servicio de todos",
      "highlights": [
        "Desarrollo de aplicacion para la solicitud de salas de reuniones ejecutivas. "
      ]
    }
  ],
  "education": [
    {
      "institution": "Instituto Aiep.",
      "area": "Programación computacional.",
      "studyType": "Tecnico",
      "startDate": "2014-01-03",
      "endDate": "2017-05-07",
      "gpa": "6.0",
      "courses": []
    }
  ],
  "awards": [],
  "publications": [],
  "skills": [
    {
      "name": " Desarrollo web",
      "level": "Semi senior.",
      "keywords": [
        "Python 2.7, 3.4",
        "Django Restful",
        "PostgreSQL",
        "PHP",
        "C#",
        "HTML5",
        "Javascripts ",
        "CSS"
      ]
    }
  ],
  "languages": [
    {
      "language": "Ingles",
      "fluency": "Intermedio-Alto"
    }
  ],
  "interests": [
    {
      "name": "Desarrollo de video juegos",
      "keywords": [
        "C++",
        "Unity ",
        "C#",
        "PythonGame"
      ]
    }
  ],
  "references": [
    {
      "name": "Jocelyn Marambio. ingenieria civil en informática ",
      "reference": "Es mi placer recomendar a David, su actuación como programador. demostró que será una adición valiosa para cualquier compañía."
    }
  ]
}
	return render(request, "resume.html" , {"myresume":myresume})
