from django.contrib import admin

# Register your models here.
from .models import Activity

class ActivityModelAdmin(admin.ModelAdmin):
	list_display = ["id", "asunto", "descripcion", "user_asign", "image", "updated","fecha_inicio", "fecha_termino",]
	list_display_links = ["user_asign",]
	list_editable = ["asunto",  "descripcion",]
	list_filter = ["asunto", "fecha_inicio", "user_asign", ]

	search_fields = ["asunto", "user_asign"]
	class Meta:
		model = Activity





admin.site.register(Activity, ActivityModelAdmin)



