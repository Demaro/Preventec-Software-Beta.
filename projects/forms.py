from django import forms

from pagedown.widgets import PagedownWidget

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project


        fields = [

			"user",

			"gerente",
			"admindor",
			"supervisor",
			"image",


		]