from django import forms

from pagedown.widgets import PagedownWidget

from .models import Modular


class ModuloForm(forms.ModelForm):
	class Meta:
		model = Modular


		fields = [
			"modules",



		]






