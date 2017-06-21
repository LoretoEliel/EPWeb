from django.contrib import admin

from foro.models import *
# Register your models here.

class AdminForoBox(admin.ModelAdmin):
	list_display = ['__unicode__' , 'user' , 'enviado']

	class Meta:
		model = Chat
admin.site.register(Chat, AdminForoBox)		