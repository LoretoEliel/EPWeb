#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class InfoForm(forms.Form):

	css_error_class = 'has-error'
	
	class Meta:
		model = subir_info

		fields = ('titulo', 'contenido')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})