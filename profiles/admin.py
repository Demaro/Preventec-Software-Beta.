from django.contrib import admin

# Register your models here.
from .models import Profile, Perfil_Obrero, Cargo, Especialidad, Especialidad_staff, Unidad

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["id", "number","user", "rut", "unidad", "birthdate","avatar", "ultimateupdate",  "cargo", "especialidad", "supervisor", "comite_par",  "subcta", "inicio_cargo", "años_exp", "contrato", "legales_asoc"]
	list_display_links = ["user"]
	list_editable = ["number", "birthdate", "rut"]
	list_filter = ["cargo", "contrato", "legales_asoc"]

	search_fields = ["user", "rut", "cargo", "contrato", "años_exp"]
	class Meta:
		model = Profile


class PerfilObreroModelAdmin(admin.ModelAdmin):
	list_display = ["id", "nombre", "apellido", "rut", "unidad", "birthdate","avatar", "ultimateupdate",  "cargo", "especialidad", "comite_par", "supervisor", "inicio_cargo", "años_exp", "contrato", "legales_asoc"]
	list_display_links = ["nombre"]
	list_editable = ["birthdate", "rut"]
	list_filter = ["cargo", "especialidad", "contrato", "legales_asoc"]

	search_fields = ["nombre", "apellido", "rut", "cargo", "contrato", "años_exp"]
	class Meta:
		model = Perfil_Obrero






class CargoModelAdmin(admin.ModelAdmin):
	list_display = ["nombre", ]
	list_editable = ["nombre", ]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Cargo


class EspecialidadStaffModelAdmin(admin.ModelAdmin):
	list_display = ["nombre"]
	list_editable = ["nombre"]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Especialidad_staff


class EspecialidadModelAdmin(admin.ModelAdmin):
	list_display = ["nombre"]
	list_editable = ["nombre"]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Especialidad


class UnidadModelAdmin(admin.ModelAdmin):
	list_display = ["nombre"]
	list_editable = ["nombre"]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Unidad





admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Perfil_Obrero, PerfilObreroModelAdmin)
admin.site.register(Cargo, CargoModelAdmin)
admin.site.register(Unidad, UnidadModelAdmin)
admin.site.register(Especialidad_staff, EspecialidadStaffModelAdmin)
admin.site.register(Especialidad, EspecialidadModelAdmin)
