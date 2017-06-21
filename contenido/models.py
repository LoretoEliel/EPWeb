from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class subir_info(models.Model):
	titulo = models.CharField(max_length=150, blank=True, null=True)
	contenido = models.TextField(max_length=2000, blank=True, null=True)
	usuario = models.ForeignKey(User)
	subida = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		Info = "%s"%(self.titulo)
		return Info