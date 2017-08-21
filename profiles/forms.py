from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from datetime import date
from django.forms import widgets, SelectDateWidget


from profiles.models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile

		fields = [
			"rut",
			"birthdate",
			"avatar",
			"cargo",
			"contrato",
			"legales_asoc",

		]
