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
	principal,

	tres,
	cuatro,
	cinco,
	seis,
	siete


	)

from posts.views import post_create

from projects.views import project_create

from django.contrib import admin

urlpatterns = [


	url(r'^admin/', admin.site.urls),

	url(r'^principal', principal, name='principal'),
	url(r'^create_post', post_create, name='create'),
	url(r'^create_project', project_create, name='create_project'),
	url(r'^table', tres, name='tabla'),
	url(r'^graphy', cuatro, name='cuatro'),
	url(r'^icons', cinco, name='cinco'),
	url(r'^dropp', seis, name='seis'),
	url(r'^notific', siete, name='siete'),

	url(r'^profiles', profile_list, name='list'),
	url(r'^crear_perfil/(?P<id_user>\d+)/$', profile_create, name="crear_perfil"),
	url(r'^perfil-detalle/(?P<id_profile>\d+)/$', profile_detail, name='detail'),
	url(r'^perfil-editar/(?P<id_profile>\d+)/$', profile_update, name='update'),

	url(r'^delete-profile/(?P<id_profile>\d+)$', profile_delete, name='delete'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
	#url(r'^resume', resume, name='resume'),


	#url(r'^posts/$', "<appname>.views.<function_name>"),
]
