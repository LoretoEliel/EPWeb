from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class libro(models.Model):
	titulo = models.CharField(max_length=150, blank=True, null=True, unique=True)
	escritor = models.CharField(max_length=150, blank=True, null=True)
	descripcion = models.TextField(max_length=5000, blank=True, null=True)
	libro = models.URLField(max_length=2000, null=True, blank=True, default='', unique=True)
	categoria = models.CharField(max_length=150, null=True, blank=True)
	subida = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(editable=False)
	autor = models.ForeignKey(User)

	def __unicode__(self):
		Info = "%s"%(self.titulo)
		return Info

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(libro, self).save(*args, **kwargs)
