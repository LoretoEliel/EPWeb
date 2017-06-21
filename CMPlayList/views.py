#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView, TemplateView
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
# from .forms import FormularioEvento
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import MusicaForm
# Buscador

from .models import musica
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

@login_required()
def index_music(request):
	queryset_list = musica.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(genero__icontains=query)|
			Q(nom_musi__icontains=query)|
			Q(nom_gru_o_art__icontains=query)
		).distinct()
	paginator = Paginator(queryset_list, 100)
	Page_reques_var = "page"
	page = request.GET.get(Page_reques_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	contexto = {
		'object_list':queryset,
		'musica':'List',
		'nom_musi' : 'List',
		'nom_gru_o_art': 'List',
		'genero': 'List',
		'usuario': 'List',
		'Page_reques_var': Page_reques_var
	}
	return render_to_response('index_music.html', contexto,
		context_instance=RequestContext(request))

@login_required()
def Agregar_Musica(request):
    #REGISTRAR O SUBIR MIS CANCIONES
    if request.method == 'POST':
    	form = MusicaForm(request.POST)
    	if form.is_valid():
    		newdoc = musica(nom_gru_o_art = request.POST['nom_gru_o_art'], 
                            nom_musi = request.POST['nom_musi'],
                            genero = request.POST['genero'],
                            musica = request.POST['musica'],
        		            usuario = request.user)
    		newdoc.save(form)
    		return redirect("Add_musica")
    else:
		form = MusicaForm()

		contexto = {
			'form': form,
		}
    
    return render(request, 'agregar_musica.html', contexto)