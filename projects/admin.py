from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ["id", "nombre", "direccion", "tipo", "image", "updated","gerente", "admindor", "supervisor", "fecha_inicio", "fecha_termino", ]
	list_display_links = ["updated", "direccion",]
	list_editable = ["nombre"]
	list_filter = ["nombre", "updated", "tipo", ]

	search_fields = ["nombre", "tipo"]
	class Meta:
		model = Project


admin.site.register(Project, ProjectModelAdmin)

