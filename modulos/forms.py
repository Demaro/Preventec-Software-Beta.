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
			
			


		]
		labels = {
			"user_asign" : 'Responsable',
			"fecha_inicio":	'Fecha inicio',
			"fecha_termino": 'Fecha Termino',									
		}
		widgets = {
			'user_asign':		forms.Select(attrs={'class': 'form-control'}),
			'fecha_inicio': 	forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_termino':	forms.TextInput(attrs={'class': 'form-control'}),
	
		}




