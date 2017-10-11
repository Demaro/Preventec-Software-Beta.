from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from datetime import date
from django.forms import widgets, SelectDateWidget


from profiles.models import Profile


class ProfileForm(forms.ModelForm):
	birthdate	= forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))
	class Meta:
		model = Profile

		fields = [
			"rut",
			"birthdate",
			"avatar",
			"cargo",

		]
		widgets = {
            'rut':   forms.TextInput(attrs={'class': 'form-control'}),
			'cargo':    forms.Select(attrs={'class': 'form-control'}),

    
        }   

class ProfileDocForm(forms.ModelForm):
	class Meta:
		model = Profile

		fields = [
			"contrato",
			"legales_asoc",

		]
		widgets = {
            'contrato':   forms.FileInput(attrs={'class': 'form-control'}),
			'legales_asoc':    forms.FileInput(attrs={'class': 'form-control'}),

    
        }  

