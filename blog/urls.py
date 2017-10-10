"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Import the include() function: from django.conf.urls import url, include
	3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth.views import login_required

from accounts.views import (login_view, register_view, logout_view, view_users) 
from django_js_reverse.views import urls_js 

from profiles import urls

from profiles.views import home

urlpatterns = [
	
	url(r'^admin/', admin.site.urls),

	url(r'^login', login_view, name='login'),
	url(r'^logout/', logout_view, name='logout'),

	url(r'^$', home, name='home'),

	url(r'^add_staff', register_view, name='staff'),
	url(r'^gestion_usuarios', view_users, name='user'),
	url(r'^', include(urls, namespace='profile')),

	#url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),

	url(r'^api/posts/', include("posts.api.urls", namespace='posts-api')),
	#url(r'^posts/$', "<appname>.views.<function_name>"),
	url(r'^jsreverse/$', (urls_js), name='js_reverse'),




]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)