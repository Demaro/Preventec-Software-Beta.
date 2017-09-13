from django.contrib import admin

# Register your models here.
from .models import Modulo, Submodulo, Carpeta



class ModuloModelAdmin(admin.ModelAdmin):
	list_display = ["id", "user_prev", "nombre", "porcent", "estado", ]
	list_display_links = ["user_prev", ]
	list_editable     = [ "nombre", "porcent", "estado", ]
	list_filter	       = [ "nombre" , "estado", ]
	filter_horizontal = [ "submodulo", ]

	search_fields = ["nombre", "user_prev"]
	class Meta:
		model = Modulo 


class SubModuloModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre", "porcent", "estado", ]
	list_editable     = [ "nombre", "porcent", "estado",  ]
	list_filter	       = [  "nombre" , "estado", ]
	filter_horizontal = [ "carpetas", ]

	search_fields = ["nombre", "estado"]
	class Meta:
		model = Submodulo


class CarpetaModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre",  "fecha_inicio", "fecha_termino", "estado",  ]
	list_editable     = [ "nombre", "estado",  "fecha_termino", "estado", ]
	list_filter	       = [  "nombre" , "estado", ]

	search_fields = ["nombre", "estado"]
	class Meta:
		model = Carpeta







admin.site.register(Modulo, ModuloModelAdmin)

admin.site.register(Submodulo, SubModuloModelAdmin)

admin.site.register(Carpeta, CarpetaModelAdmin)


