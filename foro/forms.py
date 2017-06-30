#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):

	class Meta:
		model = Chat
			
		fields = [
			'mensaje',
		]

		widgets = {
		 	'mensaje': forms.TextInput(attrs={'class':'form-control'}),
		}