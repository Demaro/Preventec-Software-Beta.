from django.conf.urls import url
from django.contrib import admin

from profiles.views import (
	profile_list,
	crear_perfil_staff,
	perfil_datos_staff2,
	perfil_datos_staff,
	carga_docu,
	carga_docu2,
	profile_detail,
	profile_update,

	crear_perfil_obrero,
	perfil_datos_obrero,
	carga_docu_obrero,
	profile_detail_obrero,
	profile_update_obrero,


	profile_delete,
	#resume,
	home,

	actividades,
	detail_actividad,
	modules,
	principal,
	profiles_contacts,
	casa


	)

from modulos.views import (
	PDFPrueba, 
	modulo_detail, 
	carpeta_detail, 
	submodulo_detail, 
	proceso_detail, 
	subcarpeta_detail, 
	subcarpeta_edit, 
	documento_select, 
	documento_select_save,
	select_users, 
	select_users2, 
	firmas_asist, 
	huellero, 
	docu_generate

	)

from modulos.views import calendar_activity

from projects.views import project_create, projects_list

from django.contrib import admin
from django.contrib.auth.views import login_required


urlpatterns = [


	url(r'^profiles', profile_list, name='list'),
	url(r'^organigrama', profiles_contacts, name='org_users'),
	url(r'^crear_perfil_staff/(?P<id_user>\d+)/$', login_required(crear_perfil_staff), name="perfil_staff"),
	url(r'^perfil_datos_staff/(?P<id_profile>\d+)/$', login_required(perfil_datos_staff), name="datos_staff"),
	url(r'^perfil_datos_staff_edit/(?P<id_profile>\d+)/$', login_required(perfil_datos_staff2), name="datos_staff2"),
	url(r'^cargar_documentos/(?P<id_profile>\d+)/$', login_required(carga_docu), name="add_docu"),
	url(r'^cargar_documentos_edit/(?P<id_profile>\d+)/$', login_required(carga_docu2), name="add_docu2"),

	url(r'^add_obrero/$', login_required(crear_perfil_obrero), name="add_obrero"),
	url(r'^perfil_datos_obrero/(?P<id_profile>\d+)/$', login_required(perfil_datos_obrero), name="datos_obrero"),
	url(r'^cargar_documentos_obrero/(?P<id_profile>\d+)/$', login_required(carga_docu_obrero), name="add_docu_obrero"),




	url(r'^perfil-detalle/(?P<id_profile>\d+)/$', login_required(profile_detail), name='profile_detail'),
	url(r'^perfil-detalle_obrero/(?P<id_profile>\d+)/$', login_required(profile_detail_obrero), name='profile_detail_obrero'),
	url(r'^perfil-editar/(?P<id_profile>\d+)/$', login_required(profile_update), name='edit'),
	url(r'^perfil-editar_obrero/(?P<id_profile>\d+)/$', login_required(profile_update_obrero), name='edit_obrero'),

	url(r'^delete-profile/(?P<id_profile>\d+)$', profile_delete, name='delete'),


	url(r'^admin/', admin.site.urls),

	url(r'^home', home, name='home'),
	url(r'^inicio', principal, name='inicio'),
	url(r'^Bienvenido', casa, name='casa'),


	url(r'^create_project', login_required(project_create), name='create_project'),
	url(r'^proyectos', login_required(projects_list), name='projects_list'),


	url(r'^actividades', login_required(actividades), name='activitys'),
	url(r'^detalle_actividad', login_required(detail_actividad), name='detail_activity'),
	url(r'^calendario_actividades', calendar_activity, name='calendar_activity'),

	url(r'^modulos', modules, name='modules'),
	url(r'^modulo/(?P<id_modulo>\d+)/$', modulo_detail, name='module'),
	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/$', submodulo_detail, name='submodule'),
	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/proceso/(?P<id_carpeta>\d+)/$', proceso_detail, name='proceso'),
	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/$', carpeta_detail, name='carpeta'),
	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/proceso/(?P<id_carpeta>\d+)/subcarpeta/(?P<id_subcarpeta>\d+)/$', subcarpeta_detail, name='subcarpeta'),
	url(r'^editar/subcarpeta/(?P<id_subcarpeta>\d+)/$', subcarpeta_edit, name='edit_subcpa'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/modelo/(?P<id_doc>\d+)/$', documento_select, name='documento'),
	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/modelo/(?P<id_doc>\d+)/docu/(?P<id_doc1>\d+)/$', documento_select_save, name='documento_save'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/modelo/(?P<id_doc>\d+)/documento/(?P<id_docu>\d+)/selecion_asistentes/$', select_users, name='select_users'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/documento/(?P<id_docu>\d+)/(?P<id_doc>\d+)/$', docu_generate, name='docu_generate'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/firmar/(?P<id_docu>\d+)/(?P<id_doc>\d+)/$', huellero, name='huella'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/firmas_asist/(?P<id_docu>\d+)/(?P<id_doc>\d+)/$', firmas_asist, name='firmas_asist'),

	url(r'^documento_pdf/(?P<id_docu>\d+)/(?P<nombre>[\w-]+)$', PDFPrueba.as_view(), name='mi_pdf'),

	url(r'^modulo/(?P<id_modulo>\d+)/submodulo/(?P<id_submodulo>\d+)/carpeta/(?P<id_carpeta>\d+)/seleccion_participantes/$', login_required(select_users2), name='select_users2'),









	#url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
	#url(r'^resume', resume, name='resume'),


	#url(r'^posts/$', "<appname>.views.<function_name>"),
]
