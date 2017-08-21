from django import forms

from pagedown.widgets import PagedownWidget

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project


        fields = [

        	"nombre",
        	"tipo",
        	"direccion",
        	"dotacion_max",
			"gerente",
			"admindor",
			"supervisor",
			"image",


		]