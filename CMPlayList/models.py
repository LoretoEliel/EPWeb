#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class musica(models.Model):
	nom_gru_o_art = models.CharField(max_length=100, null=True, blank=True)
	nom_musi = models.CharField(max_length=50, null=True, blank=True)
	genero = models.CharField(max_length=100, null=True, blank=True)
	musica = models.URLField(max_length=1000000000, null=True, blank=True, default='')
	usuario = models.ForeignKey(User)
	tiempo_registro_musica = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado_musica = models.DateTimeField(auto_now_add=False, auto_now=True)	

	def __unicode__(self):
		Dato ="%s"%(self.musica)
		return Dato