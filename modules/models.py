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
from profiles.models import Profile



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
	user_prev = models.ForeignKey(User, related_name="superuser")
	nombre    = models.CharField(max_length=100)
	porcent   = models.IntegerField(default=0)
	estado    = models.CharField(max_length=20, null=True, blank=True)
	submodulo = models.ManyToManyField('Submodulo', related_name="sub1")

	def __str__(self):
		return self.nombre



class Submodulo(models.Model):
	nombre    = models.CharField(max_length=100, null=True, blank=True)
	porcent   = models.IntegerField(default=0)
	estado    = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.nombre


class Carpeta(models.Model):
	user_asign = models.ForeignKey(User, related_name="responsable")
	nombre     = models.CharField(max_length=100)
	fecha_inicio = models.DateTimeField(null=True, blank=True)
	fecha_termino = models.DateTimeField(null=True, blank=True)
	porcent			= models.IntegerField(default=0)
	estado        = models.CharField(max_length=20)














