from django.conf.urls import url
from django.contrib import admin

from profiles.views import (
	profile_list,
	profile_create,
	profile_detail,
	profile_update,
	profile_delete,
	#resume,
	home,

	actividades,
	detail_actividad,
	modules,
	principal,
	profiles_contacts,


	)

from modulos.views import modulo_detail, carpeta_detail

from activitys.views import activity_create

from projects.views import project_create, projects_list

from django.contrib import admin
from django.contrib.auth.views import login_required

urlpatterns = [


	url(r'^profiles', profile_list, name='list'),
	url(r'^perfiles', profiles_contacts, name='profiles_contacts'),
	url(r'^perfil_crear/(?P<id_user>\d+)/$', login_required(profile_create), name="crear_perfil"),
	url(r'^perfil-detalle/(?P<id_profile>\d+)/$', login_required(profile_detail), name='detail'),
	url(r'^perfil-editar/(?P<id_profile>\d+)/$', login_required(profile_update), name='edit'),

	url(r'^delete-profile/(?P<id_profile>\d+)$', profile_delete, name='delete'),


	url(r'^admin/', admin.site.urls),

	url(r'^home', home, name='home'),
	url(r'^inicio', principal, name='inicio'),



	url(r'^create_project', login_required(project_create), name='create_project'),
	url(r'^proyectos', login_required(projects_list), name='projects_list'),


	url(r'^actividades', login_required(actividades), name='activitys'),
	url(r'^detalle_actividad', login_required(detail_actividad), name='detail_activity'),
	url(r'^calendario_actividades', activity_create, name='calendar_activity'),

	url(r'^modulos', modules, name='modules'),
	url(r'^modulo/(?P<id_modulo>\d+)/$', modulo_detail, name='module'),
	url(r'^modulo/(?P<id_modulo>\d+)/carpeta/(?P<id_carpeta>\d+)/$', carpeta_detail, name='carpeta'),




	#url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
	#url(r'^resume', resume, name='resume'),


	#url(r'^posts/$', "<appname>.views.<function_name>"),
]
