from django.contrib import admin

# Register your models here.
from .models import Activity

class ActivityModelAdmin(admin.ModelAdmin):
	list_display = ["id", "user_asign", "image", "updated","fecha_inicio", "fecha_termino",]
	list_display_links = ["user_asign",]
	list_editable = [ "fecha_termino", ]
	list_filter = [ "fecha_inicio", "user_asign", ]
	filter_horizontal = [ "carpeta", ]

	search_fields = ["user_asign"]
	class Meta:
		model = Activity





admin.site.register(Activity, ActivityModelAdmin)



