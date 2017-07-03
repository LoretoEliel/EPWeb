from django.contrib import admin

from .models import *
# Register your models here.

class AdminLibro(admin.ModelAdmin):
	list_display = ['__unicode__',
					'escritor',
					'descripcion',
					'libro',
					'categoria',
					'subida',
					'actualizado',
					'autor']

	class Meta:
		model = libro
admin.site.register(libro, AdminLibro)
