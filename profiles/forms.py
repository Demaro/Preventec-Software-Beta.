from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from datetime import date
from django.forms import widgets, SelectDateWidget


from .models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile

		fields = [
			"rut",
			"birthdate",
			"avatar",
			"cargo",
			"especialidad",
			"contrato",
			"legales_asoc",

		]
