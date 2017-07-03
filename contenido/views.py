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
	return render_to_response('index.html')

@login_required()
def home(request):
	queryset_list = libro.objects.all().order_by('-subida')
	Page_reques_var = "page"
	busqueda = request.GET.get("q")
	if busqueda:
			queryset_list = queryset_list.filter(
				Q(titulo__icontains=busqueda)|
				Q(escritor__icontains=busqueda)|
				Q(categoria__icontains=busqueda)
			).distinct()
	paginator = Paginator(queryset_list, 10)
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
		'descripcion' : 'List',
		'libro': 'List',
		'escritor': 'List',
		'categoria': 'List',
		'subida': 'List',
		'autor': 'List',
		'Page_reques_var': Page_reques_var
	}
	return render_to_response('home.html', contexto, context_instance=RequestContext(request))

@login_required()
def MisLibros(request):
	queryset_list = libro.objects.all().order_by('-subida')
	Page_reques_var = "page"
	busqueda = request.GET.get("q")
	if busqueda:
	        queryset_list = queryset_list.filter(
	            Q(titulo__icontains=busqueda)|
				Q(escritor__icontains=busqueda)|
				Q(categoria__icontains=busqueda)
	        ).distinct()
	paginator = Paginator(queryset_list, 10)
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
		'escritor': 'List',
		'libro': 'List',
		'categoria': 'List',
		'subida': 'List',
		'autor': 'List',
		'Page_reques_var': Page_reques_var
	}
	return render_to_response('mis_libros.html', contexto, context_instance=RequestContext(request))

@login_required()
def UploadLibro(request):
	if request.method == 'POST':
		form = libroForm(request.POST)
		if form.is_valid():
			newdoc = libro(titulo = request.POST['titulo'],
						   escritor = request.POST['escritor'],
        				   descripcion = request.POST['descripcion'],
						   libro = request.POST['libro'],
						   categoria = request.POST['categoria'],
						   autor = request.user)
			newdoc.save(form)
			return HttpResponseRedirect('/libro_guardado/')
	else:
		form = libroForm()

	contexto = {
    	'form': form,
    }
    	return render(request, 'agregar_libro.html', contexto)

@login_required()
def libro_guardado(request):
	return render_to_response("libro_guardado.html")

@login_required()
def eliminar_libro(request, pk):
	info = get_object_or_404(libro, pk=pk)
	info.delete()
	return redirect('MisLibros')
