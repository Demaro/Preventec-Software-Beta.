from django.conf import settings
from rest_framework import serializers

from profiles.models import Profile
from accounts.serializers import UserSerializer
from accounts.serializers import UserSerializer



class PerfilSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)



	class Meta:
		model = Profile
		fields = ('user', 'rut', 'birthdate', 'ultimateupdate', 'comite_par', 'subcta', 'cargo', 'especialidad', 'supervisor', )


