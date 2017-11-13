from django.contrib import admin

# Register your models here.
from .models import Music

class MusicModelAdmin(admin.ModelAdmin):
	list_display = ["id", "nombre", "user_asign", "last_modify_date", "created", ]
	list_display_links = ["id", ]
	list_editable     = [ "nombre", ]
	list_filter	       = [ "nombre" , "user_asign", ]

	class Meta:
		model = Music 




admin.site.register(Music, MusicModelAdmin)

	


