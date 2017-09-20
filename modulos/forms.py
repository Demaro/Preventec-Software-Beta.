from django import forms

from pagedown.widgets import PagedownWidget

from .models import Modulo, Carpeta


class ModuloForm(forms.ModelForm):
	class Meta:
		model = Modulo


		fields = [
			"submodulo",



		]


class CarpetaForm(forms.ModelForm):
	class Meta:
		model = Carpeta


		fields = [
			"user_asign",
			"fecha_inicio",
			"fecha_termino",
			"estado"



		]




