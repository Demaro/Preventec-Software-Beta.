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
    dos,
    tres,
    cuatro,
    cinco,
    seis,
    siete


    )

from accounts.views import login_view, logout_view
from django.contrib import admin

urlpatterns = [


    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^principal', principal, name='principal'),
    url(r'^users', dos, name='dos'),
    url(r'^table', tres, name='tres'),
    url(r'^grafic', cuatro, name='cuatro'),
    url(r'^shortcode', cinco, name='cinco'),
    url(r'^dropp', seis, name='seis'),
    url(r'^dropp', siete, name='siete'),

    url(r'^profiles', profile_list, name='list'),
    url(r'^crear_perfil/(?P<id_user>\d+)/$', profile_create, name="crear_perfil"),
    url(r'^perfil-detalle/(?P<id_profile>\d+)/$', profile_detail, name='detail'),
    url(r'^perfil-editar/(?P<id_profile>\d+)/$', profile_update, name='update'),

    url(r'^delete-profile/(?P<id_profile>\d+)$', profile_delete, name='delete'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    #url(r'^resume', resume, name='resume'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
