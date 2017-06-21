#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class MusicaForm(forms.Form):
	
	class Meta:
		model = musica

		fields = ('nom_gru_o_art', 'nom_musi', 'genero', 'musica')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})