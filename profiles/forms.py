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
		labels	=	{
			"rut":			"Rut",
			"birthdate":	"Fecha nacimiento",
			"cargo":		"Cargo",
			"especialidad":	"Especialidad",
			"contrato":		"Contrato",
			"legales_asoc": "Asuntos legales adociados",


		}
		widgets	=	{

			"birthdate":	forms.DateInput(attrs={'class': 'form-control'}),
			"cargo":		forms.Select(attrs={'class': 'form-control'}),
			"especialidad":	forms.Select(attrs={'class': 'form-control'}),
			"contrato":		forms.TextInput(attrs={'class': 'form-control'}),
			"legales_asoc": forms.TextInput(attrs={'class': 'form-control'}),

		}