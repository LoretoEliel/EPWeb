#-*- coding:utf-8 -*-
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

class AdminMusi(admin.ModelAdmin):
	list_display = ['__unicode__',
					'nom_gru_o_art',
					'nom_musi',
					'genero',
					'usuario',
					'tiempo_registro_musica',
					'actualizado_musica']
	class Meta:
		model = musica
admin.site.register(musica, AdminMusi)
