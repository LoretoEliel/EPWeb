from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    enviado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    mensaje = models.CharField(max_length=5000)

    def __unicode__(self):
    	Dato ="%s"%(self.mensaje)
        return Dato