from django.contrib import admin

from .models import *
# Register your models here.

class AdminInfo(admin.ModelAdmin):
	list_display = ['__unicode__', 'contenido', 'usuario', 'subida', 'actualizado']

	class Meta:
		model = subir_info
admin.site.register(subir_info, AdminInfo)		