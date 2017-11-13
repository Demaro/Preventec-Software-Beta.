#! / Usr / bin / python env
# - * - coding: UTF-8 - * -

from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from django.contrib.auth.models import User
from markdown_deux import markdown

from profiles.models import Profile, Perfil_Obrero


from datetime import timedelta
from datetime import datetime
from django.db.models import signals
from django.db.models.signals import post_save 
from django.db.models import Count
from django.db.models import Q
from model_utils import Choices



# Create your models here.
# MVC MODEL VIEW CONTROLLER



class ModulesManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(ModulesManager, self)


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	ModulesModel = instance.__class__
	new_id = ModulesModel.objects.order_by("id").last().id + 1
	"""

	Then we get the last object in the queryset with `.last()`
	Which will give us the most recently created Model instance

	"""
	return "%s/%s" %(new_id, filename)



class Modulo(models.Model):
	user_prev 	= models.ForeignKey(User, related_name="superuser")
	default		= models.NullBooleanField(null=True, blank=True)
	nombre    	= models.CharField(max_length=100)
	porcent   	= models.IntegerField(default=0)
	estado    	= models.CharField(max_length=20, null=True, blank=True)
	submodulo 	= models.ManyToManyField('Submodulo', related_name="sub1")

	def __str__(self):
		return self.nombre


ORDER_COLUMN_CHOICES = Choices(
	('0', 'nombre'),
	('1', 'porcent'),
	('2', 'estado'),
	('3', 'carpeta'),
	('4', 'tipo')
)

class Submodulo(models.Model):
	nombre  	=	models.CharField(max_length=100, null=True, blank=True)
	default		= 	models.NullBooleanField(null=True, blank=True)
	porcent 	= 	models.IntegerField(default=0)
	estado  	= 	models.CharField(max_length=20, null=True, blank=True)
	carpeta 	= 	models.ManyToManyField('Carpeta', related_name="carpeta")
	tipo			= models.ForeignKey('Tipo', related_name="tipo_carpeta1", null=True, blank=True)
	

	def __str__(self):
		return self.nombre





class Carpeta(models.Model):
	user_asign		= models.ForeignKey(Profile, related_name="responsable", null=True, blank=True)
	default			= models.BooleanField(default=True)
	nombre     		= models.CharField(max_length=100)
	porcent			= models.IntegerField(default=0)
	estado        	= models.CharField(max_length=20)
	subcarpeta		= models.ManyToManyField('SubCarpeta', related_name="subcarpeta",  blank=True)
	fecha_inicio	= models.DateField(null=True, blank=True)
	fecha_termino	= models.DateField(null=True, blank=True)
	cumplimiento	= models.ForeignKey('Ejecucion', related_name="run", null=True, blank=True)
	submodulo 		= models.ForeignKey('Submodulo', related_name="sub2" ,null=True, blank=True)
	#archivo


	def __str__(self):
		return self.nombre


def query_carpeta_by_args(**kwargs):
	draw = int(kwargs.get('draw', None)[0])
	length = int(kwargs.get('length', None)[0])
	start = int(kwargs.get('start', None)[0])
	search_value = kwargs.get('search[value]', None)[0]
	order_column = kwargs.get('order[0][column]', None)[0]
	order = kwargs.get('order[0][dir]', None)[0]

	order_column = ORDER_COLUMN_CHOICES[order_column]
	# django orm '-' -> desc
	if order == 'desc':
		order_column = '-' + order_column

	if search_value:
		queryset = Carpeta.objects.filter(Q(id__icontains=search_value) |
										Q(nombre__icontains=search_value) |
										Q(porcent__icontains=search_value) |
										Q(user_asign__icontains=search_value) |
										Q(estado__icontains=search_value))
	else:
		queryset = Carpeta.objects
	count = queryset.count()
	queryset = queryset.order_by(order_column)[start:start + length]
	return {
		'items': queryset,
		'count': count,
		'draw': draw
	}



class Tipo(models.Model):
	nombre	=	models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class SubCarpeta(models.Model):
	default			= models.BooleanField()
	nombre     		= models.CharField(max_length=100)
	porcent			= models.IntegerField(default=0)
	estado        	= models.CharField(max_length=20)
	cumplimiento	= models.ForeignKey('Ejecucion', related_name="responsable", null=True, blank=True)
	#actividad

	def __str__(self):
		return self.nombre

class Ejecucion(models.Model):
	nombre	= models.CharField(max_length=30)

	def __str__(self):
		return self.nombre


def get_deadline():
	return datetime.today() + timedelta(days=2)



class Documento(models.Model):
	template 	= models.ForeignKey('Template', related_name="template", null=True, blank=True)
	user1	=	models.ForeignKey(Profile, related_name="user1", null=True, blank=True)
	fecha 	=	models.DateField(null=True, blank=True)
	fecha2	=	models.DateField(null=True, blank=True, default=get_deadline)
	fecha3	=	models.DateField(null=True, blank=True)
	depto	=	models.CharField(max_length=50, null=True, blank=True)
	duracion	=	models.IntegerField(default=0)
	titulo	=	models.TextField()
	descripcion	= 	models.TextField(null=True, blank=True)
	subtitulo1	=	models.TextField(null=True, blank=True)
	subtitulo2	=	models.TextField(null=True, blank=True)
	user2		=	models.ForeignKey(Profile, related_name="user2", null=True, blank=True)
	firmas 		=	models.ManyToManyField(Profile,  blank=True)
	firmasobr   =	models.ManyToManyField(Perfil_Obrero,  blank=True)
	suma_firmas	= 	models.IntegerField(null=True, blank=True, default=0)
	etapa		=  	models.IntegerField(null=True, blank=True, default=0)
	default 	=	models.BooleanField(default=False)

	def __str__(self):
		return self.titulo

	def get_markdown(self):
		descripcion = self.descripcion
		markdown_text = markdown(descripcion)
		return mark_safe(markdown_text)




class Template(models.Model):
	nombre = models.CharField(max_length=20)
	

	def __str__(self):
		return self.nombre

		




