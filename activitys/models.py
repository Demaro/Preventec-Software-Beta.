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
from comments.models import Comment
from profiles.models import Profile



# Create your models here.
# MVC MODEL VIEW CONTROLLER



class ActivityManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(ActivityManager, self)


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	ActivityModel = instance.__class__
	new_id = ActivityModel.objects.order_by("id").last().id + 1
	"""

	Then we get the last object in the queryset with `.last()`
	Which will give us the most recently created Model instance

	"""
	return "%s/%s" %(new_id, filename)

class Activity(models.Model):
	user_create = models.ForeignKey(User,related_name="user_create")
	asunto = models.CharField(max_length=20)
	descripcion   = models.CharField(max_length=20)
	user_asign = models.ForeignKey(User,related_name="asignado")

	slug = models.SlugField(unique=True, null=True)
	image = models.ImageField(upload_to=upload_location, 
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	fecha_inicio = models.DateField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	fecha_termino = models.DateTimeField(null=True, blank=True)


	objects = ActivityManager()

	def __unicode__(self):
		return self.asunto

	def __str__(self):
		return self.asunto









