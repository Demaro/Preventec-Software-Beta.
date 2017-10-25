from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from datetime import date
from django.forms import widgets, SelectDateWidget


from profiles.models import Profile, Perfil_Obrero


class ProfileForm(forms.ModelForm):
	birthdate	= forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))
	class Meta:
		model = Profile

		fields = [
			"rut",
			"birthdate",
			"avatar",


		]
		widgets = {
            'rut':   forms.TextInput(attrs={'class': 'form-control'}),


    
        }   

class ProfileDatosForm(forms.ModelForm):
	inicio_cargo	= forms.DateField(widget=forms.SelectDateWidget(years=range(2017, 2020)))
	class Meta:
		model = Profile

		fields = [
			"cargo",
			"unidad",
			"comite_par",
			"subcta",
			"inicio_cargo",

		]
		widgets = {
            'cargo':   forms.Select(attrs={'class': 'form-control'}),
			'unidad':    forms.Select(attrs={'class': 'form-control'}),
			'comite_par': forms.CheckboxInput(attrs={'class': 'form-control'}),
			'subcta'	:	forms.CheckboxInput(attrs={'class': 'form-control'}),



    
        } 

class ProfileDocForm(forms.ModelForm):
	class Meta:
		model = Profile

		fields = [
			"contrato",
			"legales_asoc",

		]
		widgets = {
            'contrato':   forms.FileInput(attrs={'class': 'form-control'}),
			'legales_asoc':    forms.FileInput(attrs={'class': 'form-control'}),

    
        }  


# Perfil Obrero:

class ProfileObreroForm(forms.ModelForm):
	birthdate	= forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))
	class Meta:
		model = Perfil_Obrero

		fields = [
			"nombre",
			"apellido",
			"rut",
			"birthdate",


		]
		widgets = {
            'nombre':   forms.TextInput(attrs={'class': 'form-control'}),
            'apellido':   forms.TextInput(attrs={'class': 'form-control'}),
            'rut':   forms.TextInput(attrs={'class': 'form-control'}),


    
        } 


class ProfileDatosObreroForm(forms.ModelForm):
	inicio_cargo	= forms.DateField(widget=forms.SelectDateWidget(years=range(2017, 2020)))
	class Meta:
		model = Perfil_Obrero

		fields = [

			"especialidad",
			"unidad",
			"comite_par",
			"supervisor",
			"inicio_cargo",

		]
		widgets = {
            'especialidad':   forms.Select(attrs={'class': 'form-control'}),
            'supervisor':		forms.Select(attrs={'class': 'form-control'}),
			'unidad':    forms.Select(attrs={'class': 'form-control'}),
			'comite_par': forms.CheckboxInput(attrs={'class': 'form-control'}),




    
        } 

class ProfileDocObreroForm(forms.ModelForm):
	class Meta:
		model = Perfil_Obrero

		fields = [
			"contrato",
			"legales_asoc",

		]
		widgets = {
            'contrato':   forms.FileInput(attrs={'class': 'form-control'}),
			'legales_asoc':    forms.FileInput(attrs={'class': 'form-control'}),

    
        }





