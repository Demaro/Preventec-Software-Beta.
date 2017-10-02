from django import forms

from pagedown.widgets import PagedownWidget

from .models import Modulo, Carpeta, SubCarpeta, Documento


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

class SubCarpetaForm(forms.ModelForm):
	class Meta:
		model = SubCarpeta


		fields = [
			"nombre",
			"porcent",
			"cumplimiento",


		]
		labels = {
			"nombre" : 'Nombre',
			"porcent":	'Porcentaje',
			"cumplimiento": 'Cumplimiento',									
		}
		widgets = {
			'nombre':		forms.TextInput(attrs={'class': 'form-control'}),
			'porcent': 		forms.NumberInput(attrs={'class': 'form-control'}),
			'cumplimiento':	forms.Select(attrs={'class': 'form-control'}),
	
		}



class DocumentoForm(forms.ModelForm):
	descripcion = forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model = Documento


		fields = [
			"user1",
			"depto",
			"duracion",
			"titulo",
			"descripcion",
			"subtitulo1",
			"subtitulo2",
			"user2",


		]
		labels = {
			"user1" :	'Nombre',
			"depto" :	'Depto',
			"duracion" :	'Duracion',
			"titulo" :	'Titulo',
			"subtitulo1" : 'Sub Titulo',
			"subtitulo2" :	'Sub Titulo',
			"user2" :		'Efectuado por'	,			
		}
		widgets = {
			'user1':		forms.Select(attrs={'class': 'form-control'}),
			'depto':		forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Depto'}),
			"duracion":	  	forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duracion'}),				
			"titulo":	  	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),	
			"subtitulo1":  	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub titulo'}),
			"subtitulo2":  	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub titulo'}),
			"user2":  		forms.Select(attrs={'class': 'form-control'}),

	
		}




