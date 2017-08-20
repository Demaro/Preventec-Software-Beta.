from django import forms

from pagedown.widgets import PagedownWidget

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project


        fields = [

			"gerente",
			"admindor",
			"supervisor",
			"image",


		]