from django import forms

from pagedown.widgets import PagedownWidget

from .models import Activity


class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity


		fields = [

			"asunto",
			"descripcion",
			"user_asign",
			"image",


		]






