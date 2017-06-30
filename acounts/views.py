#!/usr/bin/python
# -*- coding: utf-8 -*-

#________________________________________
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
#paginacion de django#

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from .forms import *
# Create your views here.

from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

def add_user(request):
    if request.method == 'POST':  # Si el formulario ha sido enviado...
        form = RegistroForm(request.POST)  # Un formulario vinculado a los datos POST
        if form.is_valid():  # Todas las reglas de validación pasan

            # Procesar los datos en form.cleaned_data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

			# En este punto, el usuario es un objeto de usuario que ya se ha guardado
            # A la base de datos. Puede seguir cambiando sus atributos
            # Si desea cambiar otros campos.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name


			# Guardar nuevos atributos de usuario
            user.save()
            return HttpResponseRedirect('/success/')    
            #tambien se puede usar
            #return HttpResponseRedirect(reverse('main.html'))  # Redirect after POST
    else:
        form = RegistroForm()

    data = {
        'form': form,
    }
    return render_to_response('registrar.html', data, context_instance=RequestContext(request))

#solo llama al html correspondiente al usuario creado
def register_success(request):
    return render_to_response('success.html')

@login_required()
def my_perfil(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su contraseña se actualizó correctamente!')
            return redirect('MyPerfil')
        else:
            messages.error(request, 'Corrija el error a continuación.')
    else:
        form = PasswordChangeForm(request.user)

    return render_to_response('mi_perfil.html', {'form': form}, context_instance=RequestContext(request))

def contacto_email(request):
    if request.method == 'POST':
        form = ContactoFrom(request.POST)
        if form.is_valid():
            asunto = 'EPWeb - Mensaje'
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            mail = EmailMessage(asunto,
                                email,
                                mensaje,
                                to = [settings.EMAIL_HOST_USER])
            mail.send()
        return HttpResponseRedirect('/email_envidado/')
    else:
        form = ContactoFrom()

    return render_to_response('contacto.html', {'form': form}, context_instance=RequestContext(request))

def contacto_exitoso(request):
    return render_to_response('contacto_exitoso.html')
