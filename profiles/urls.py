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


    )

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^/profile-list', profile_list, name='list'),
    url(r'^crear_perfil/(?P<id_user>\d+)/$', profile_create, name="crear_perfil"),
    url(r'^perfil-detalle/(?P<id_profile>\d+)/$', profile_detail, name='detail'),
    url(r'^perfil-editar/(?P<id_profile>\d+)/$', profile_update, name='update'),

    url(r'^delete-profile/(?P<id_profile>\d+)$', profile_delete, name='delete'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    #url(r'^resume', resume, name='resume'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
