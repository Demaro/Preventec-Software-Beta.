from django.contrib import admin

# Register your models here.
from .models import Modulo, Submodulo



class ModuloModelAdmin(admin.ModelAdmin):
	list_display = ["id", "user_prev", "nombre", "porcent", "estado", ]
	list_display_links = ["user_prev", ]
	list_editable     = [ "nombre", "porcent", "estado", ]
	list_filter	       = [ "nombre" , "estado", ]

	search_fields = ["nombre", "user_prev"]
	class Meta:
		model = Modulo 


class SubModuloModelAdmin(admin.ModelAdmin):
	list_display = ["id", "modulo", "nombre", "porcent", "estado", ]
	list_display_links = [ "modulo" ,]
	list_editable     = [ "nombre", "porcent", "estado",  ]
	list_filter	       = [ "modulo", "nombre" , "estado", ]

	search_fields = ["nombre", "modulo", "estado"]
	class Meta:
		model = Submodulo



admin.site.register(Modulo, ModuloModelAdmin)

admin.site.register(Submodulo, SubModuloModelAdmin)





