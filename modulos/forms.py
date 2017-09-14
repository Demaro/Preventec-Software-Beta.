from django import forms

from pagedown.widgets import PagedownWidget

from .models import Modulo


class ModuloForm(forms.ModelForm):
	class Meta:
		model = Modulo


		fields = [
			"submodulo",



		]


