from django.contrib import admin

# Register your models here.
from .models import Profile, Cargo, Especialidad

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["id", "user", "rut", "birthdate","avatar", "ultimateupdate",  "cargo", "especialidad", "inicio_cargo", "años_exp", "contrato", "legales_asoc"]
	list_display_links = ["user"]
	list_editable = ["birthdate", "rut"]
	list_filter = ["cargo", "especialidad", "contrato", "legales_asoc"]

	search_fields = ["user", "rut", "cargo", "contrato", "años_exp"]
	class Meta:
		model = Profile

class CargoModelAdmin(admin.ModelAdmin):
	list_display = ["nombre", "tipo",]
	list_editable = ["nombre", "tipo",]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Cargo

class EspecialidadModelAdmin(admin.ModelAdmin):
	list_display = ["nombre"]
	list_editable = ["nombre"]
	list_filter = ["nombre"]

	search_fields = ["nombre"]
	class Meta:
		model = Especialidad





admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Cargo, CargoModelAdmin)
admin.site.register(Especialidad, EspecialidadModelAdmin)
