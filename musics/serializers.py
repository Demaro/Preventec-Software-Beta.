from django.conf import settings
from rest_framework import serializers

from musics.models import Music

from profiles.serializers import PerfilSerializer


class MusicSerializer(serializers.ModelSerializer):
	# If your <field_name> is declared on your serializer with the parameter required=False
	# then this validation step will not take place if the field is not included.

	last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
	created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)
	user_asign = PerfilSerializer(read_only=True)

	class Meta:
		model = Music
		# fields = '__all__'
		fields = ('id', 'nombre', 'user_asign', 'last_modify_date', 'created')

