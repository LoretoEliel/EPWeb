#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class libroForm(forms.Form):

	css_error_class = 'has-error'

	class Meta:
		model = libro

		fields = ('titulo', 'escritor', 'descripcion', 'libro', 'categoria')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})
		def clean(self):
        		cleaned_data = super(libroForm, self).clean()
			title_exists = (titulo.objects.filter(titulo = cleaned_data.get('titulo')).count() > 0)

			if title_exists:
        			self.add_error('El contenido que va a subir ya existe')
