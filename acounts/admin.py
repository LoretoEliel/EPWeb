from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(login)

class reg_fotoAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']

	class Meta:
		model = reg_foto
admin.site.register(reg_foto, reg_fotoAdmin)