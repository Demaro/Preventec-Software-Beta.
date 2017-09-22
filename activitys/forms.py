from django import forms

from pagedown.widgets import PagedownWidget

from .models import Activity




class ActivityForm(forms.ModelForm):

	class Meta:
		
		model = Activity


		fields = [

			"user_asign",
			"fecha_inicio",
			"fecha_termino",
			"carpeta",
			


		]
		labels = {
			"user_asign" : 'Responsable',
			"fecha_inicio":	'Fecha inicio',
			"fecha_termino": 'Fecha Termino',
			"carpeta":		'carpeta',							
		}
		widgets = {
			'user_asign':		forms.Select(attrs={'class': 'form-control'}),
			'fecha_inicio': 	forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_termino':	forms.TextInput(attrs={'class': 'form-control'}),
			'carpeta':          forms.CheckboxSelectMultiple(attrs={'class': 'flat'}),
	
		}






