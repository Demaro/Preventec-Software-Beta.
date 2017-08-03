from django.conf.urls import url
from django.contrib import admin

from profiles.views import (
    profile_list,
    profile_create,
    #post_detail,
    #post_update,
    #post_delete,
    #resume,


    )

urlpatterns = [
    url(r'^$', profile_list, name='list'),
    url(r'^crear_perfil/(?P<id_user>\d+)/$', profile_create, name="crear_perfil"),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    #url(r'^resume', resume, name='resume'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
