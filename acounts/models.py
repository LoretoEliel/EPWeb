#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from models import *

# Create your models here.

class login(models.Model):
	user = models.ForeignKey(User)
	activo = models.BooleanField(default=False)

	def __unicode__(self):
		dato ="%s" %(self.user) #si usa python3 el unicode es irrelevante. debe modificarlo a:
		return dato		#def __str__(self):

class reg_foto(models.Model):
	foto = models.FileField(upload_to='foto_perfil/', blank=True, null=True)
	user_perfil = models.ForeignKey(User)

	def __unicode__(self):
		xxx = "%s"%(self.user_perfil)
		return xxx