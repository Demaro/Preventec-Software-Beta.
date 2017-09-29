from django.contrib import admin

# Register your models here.
from .models import Modulo, Submodulo, Carpeta, SubCarpeta, Tipo, Ejecucion



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
	filter_horizontal = [ "carpeta", ]

	search_fields = ["nombre", "estado"]
	class Meta:
		model = Submodulo


class CarpetaModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre",  "fecha_inicio", "fecha_termino", "estado", "default", "tipo",]
	list_editable     = [ "nombre",   "fecha_termino", "estado", "default", "tipo", ]
	list_filter	       = [  "nombre" , "estado", "subcarpeta",  ]
	filter_horizontal = [ "subcarpeta", ]

	search_fields = ["nombre", "estado", ]
	class Meta:
		model = Carpeta

class TipoModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre",  ]
	list_editable     = [ "nombre", ]
	list_filter	       = [  "nombre" ,  ]

	search_fields = ["nombre",  ]
	class Meta:
		model = Tipo

class SubCarpetaModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre",  "fecha_inicio", "fecha_termino", "estado", "default", "cumplimiento",]
	list_editable     = [ "nombre", "estado",  "fecha_termino", "estado", "default", "cumplimiento",]
	list_filter	       = [  "nombre" , "estado", ]

	search_fields = ["nombre", "estado", ]
	class Meta:
		model = SubCarpeta


class EjecucionModelAdmin(admin.ModelAdmin):
	list_display = ["id",  "nombre",  ]
	list_editable     = [ "nombre", ]
	list_filter	       = [  "nombre" ,  ]

	search_fields = ["nombre",  ]
	class Meta:
		model = Ejecucion








admin.site.register(Modulo, ModuloModelAdmin)

admin.site.register(Submodulo, SubModuloModelAdmin)

admin.site.register(Carpeta, CarpetaModelAdmin)

admin.site.register(Tipo, TipoModelAdmin)

admin.site.register(Ejecucion, EjecucionModelAdmin)

admin.site.register(SubCarpeta, SubCarpetaModelAdmin)
