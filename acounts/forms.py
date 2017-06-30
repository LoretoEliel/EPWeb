#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
 
 
class RegistroForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput()}

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Current Password', 'autocomplete': 'off'}))

    new_password = forms.CharField(
        min_length=6,
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password', 'autocomplete': 'off'}))

    confirm_password = forms.CharField(
        min_length=6,
        max_length=64,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm New Password', 'autocomplete': 'off'}))

class fotouser(forms.Form):
    
    css_error_class = 'has-error'
    
    class Meta:
        model = reg_foto

        fields = ('foto')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})

class ContactoFrom(forms.Form):
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=50000)   