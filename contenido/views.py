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
from django.views.generic import ListView, DeleteView, TemplateView, UpdateView
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
# from .forms import FormularioEvento
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from acounts.models import reg_foto

# Buscador
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

def index(request):
	queryset_list = subir_info.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(titulo__icontains=query)|
			Q(subida__icontains=query)
		).distinct()
	paginator = Paginator(queryset_list, 50)
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
		'titulo':'List',
		'contenido' : 'List',
		'subida': 'List',
		'usuario': 'List',
		'Page_reques_var': Page_reques_var
	}
	return render_to_response('index.html', contexto, context_instance=RequestContext(request))

@login_required()
def home(request):
	queryset_list = reg_foto.objects.all()
	queryset_list = subir_info.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(titulo__icontains=query)|
			Q(subida__icontains=query)
		).distinct()
	paginator = Paginator(queryset_list, 50)
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
		'titulo':'List',
		'contenido' : 'List',
		'subida': 'List',
		'foto': 'List',
		'usuario': 'List',
		'Page_reques_var': Page_reques_var
	}
	return render_to_response('home.html', contexto, context_instance=RequestContext(request))

@login_required()
def info(request):
	if request.method == 'POST':
		form = InfoForm(request.POST)
		if form.is_valid():
			newdoc = subir_info(titulo = request.POST['titulo'],
        						usuario = request.user,
        						contenido = request.POST['contenido'])
			newdoc.save(form)
			return HttpResponseRedirect('/info_guardada/')
	else:
		form = InfoForm()

	contexto = {
    	'form': form,
    }
    	return render(request, 'agregar_info.html', contexto)

@login_required()
def info_guardada(request):
	return render_to_response("info_guardada.html")    	

@login_required()
def eliminar_info(request, pk):

	info = get_object_or_404(subir_info, pk=pk)
	info.delete()
	return redirect('Home')    	