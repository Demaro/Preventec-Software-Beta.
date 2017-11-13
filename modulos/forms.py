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
			"nombre",
			"porcent",
			"fecha_inicio",
			"fecha_termino",
			"cumplimiento",

		]
		labels = {
								
		}
		widgets = {
			'user_asign':		forms.Select(attrs={'class': 'form-control'}),
			'nombre':			forms.TextInput(attrs={'class': 'form-control'}),
			'porcent': 			forms.NumberInput(attrs={'class': 'form-control'}),
			'fecha_termino':	forms.DateInput(attrs={'class': 'form-control'}),
			'fecha_termino':	forms.DateInput(attrs={'class': 'form-control'}),
			'cumplimiento':		forms.Select(attrs={'class': 'form-control'}),
	
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

			"fecha_termino":forms.DateInput(attrs={'class': 'form-control'}),
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


class DocFirmasForm(forms.ModelForm):
		
	class Meta:
		model = Documento


		fields = [

			"firmas",
			"firmasobr",


		]
		labels = {

			"firmas":		'',	
			"firmasobr":	'',	
		}
		widgets = {

			"firmas":  		forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox_flat-green'}),
			"firmasobr":  		forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox_flat-green2'}),

	
		}

class DocEtapaForm(forms.ModelForm):
		
	class Meta:
		model = Documento


		fields = [

			"etapa",


		]

class SumaFirmasForm(forms.ModelForm):
		
	class Meta:
		model = Documento


		fields = [

			"suma_firmas",


		]
