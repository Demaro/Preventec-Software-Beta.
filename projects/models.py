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



# Create your models here.
# MVC MODEL VIEW CONTROLLER



class ProjectManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(ProjectManager, self).filter(draft=False).filter(fecha_inicio__lte=timezone.now())


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	ProjectModel = instance.__class__
	new_id = ProjectModel.objects.order_by("id").last().id + 1
	"""

	Then we get the last object in the queryset with `.last()`
	Which will give us the most recently created Model instance

	"""
	return "%s/%s" %(new_id, filename)

class Project(models.Model):
	user = models.ForeignKey(User,related_name="user")
	nombre = models.CharField(max_length=20)
	tipo   = models.CharField(max_length=20)
	direccion = models.CharField(max_length=20)
	gerente = models.ForeignKey(User,related_name="gerente")
	admindor = models.ForeignKey(User,related_name="admindor")
	supervisor = models.ForeignKey(User,related_name="supervisor")
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, 
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	dotacion_max = models.IntegerField(default=0)
	draft = models.BooleanField(default=False)
	fecha_inicio = models.DateField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	fecha_termino = models.DateField(null=True, blank=True)


	objects = ProjectManager()

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("project:detail", kwargs={"slug": self.slug})

	def get_api_url(self):
		return reverse("projects-api:detail", kwargs={"slug": self.slug})


	def get_markdown(self):
		direccion = self.direccion
		markdown_text = markdown(direccion)
		return mark_safe(markdown_text)

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type


def create_slug(instance, new_slug=None):
	slug = slugify(instance.nombre)
	if new_slug is not None:
		slug = new_slug
	qs = Project.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_project_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_project_receiver, sender=Project)
















