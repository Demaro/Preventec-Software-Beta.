from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,
	)

from rest_framework import serializers

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
				'username',
				'email',
				'first_name',
				'last_name',
		]


class UserCreateSerializer(ModelSerializer):
	email = EmailField(label='Correo Electronico')
	email2 = EmailField(label='Confirmar Correo')
	class Meta:
		model = User
		fields = [
				'username',
				'email',
				'email2',
				'password',

		]
		extra_kwargs = {"password":
							{"write_only": True}
							}

	#def validate_email(self, value):
		#email = data['email']
		#user_qs = User.objects.filter(email=email)
		#if user_qs.exisist():
		#	raise ValidationError("Este usuario ya esta registrado.")
		#return data


	def validate_email(self, value):
		data = self.get_initial()
		email1 = data.get("email2")
		email2 = value
		if email1 != email2:
			raise ValidationError("Correos no coincide.")

		user_qs = User.objects.filter(email=email2)
		if user_qs.exisist():
			raise ValidationError("Este usuario ya esta registrado.")
		return value

	def validate_email2(self, value):
		data = self.get_initial()
		email1 = data.get("email")
		email2 = value
		if email1 != email2:
			raise ValidationError("Correos no coincide.")
		return value

	def create(self, validated_data):
		username = validated_data['username']
		email    = validated_data['email']
		password = validated_data['password']
		user_obj = User(
				username = username,
				email = email
				)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True)
	class Meta:
		model = User
		fields = [
				'username',
				'password',
				'token',

		]
		extra_kwargs = {"password":
							{"write_only": True}
							}

	def validate(self, data):
		user_obj = None
		username = data.get("username", None)
		password = data["password"]
		if not username:
			raise ValidationError("ingrese usuario o contraseña")

		user = User.objects.filter(
#				Q(email=email) |
				Q(username=username)
			).distinct()
#		user = user.exclude(email__isnull=True).exclude(email___iexact='')
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else: 
			raise ValidationError("Usuario no valido.")
		
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("credecianles incorrectas, porfavor vuelva a intentar.")

		data["token"] = "SOME RANDONM TOKEN"

		return data

