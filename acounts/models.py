#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from models import *

# Create your models here.

class login(models.Model):
	username = models.CharField(max_length=25, null=True)
	password = models.CharField(max_length=25, null=True)
	email = models.CharField(max_length=25, null=True)
	first_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)

	def __unicode__(self):
		dato ="%s" %(self.username) #si usa python3 el unicode es irrelevante. debe modificarlo a:
		return dato		#def __str__(self):

class reg_foto(models.Model):
	foto = models.FileField(upload_to='foto_perfil/', blank=True, null=True)
	user_perfil = models.ForeignKey(User)

	def __unicode__(self):
		xxx = "%s"%(self.user_perfil)
		return xxx