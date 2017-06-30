from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class libro(models.Model):
	titulo = models.CharField(max_length=150, blank=True, null=True)
	descripcion = models.TextField(max_length=5000, blank=True, null=True)
	libro = models.URLField(max_length=2000, null=True, blank=True, default='')
	categoria = models.CharField(max_length=150, null=True, blank=True)
	subida = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	autor = models.ForeignKey(User)

	def __unicode__(self):
		Info = "%s"%(self.titulo)
		return Info
