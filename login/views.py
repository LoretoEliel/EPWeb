# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from acounts import models
from django.http import HttpResponse
# Create your views here.
# Login
class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", { 'form': form })

    def post(self, request):
    	form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
        	if user.is_active:
        		vali = models.login.objects.get(user=user.pk)
        		vali.activo=True
        		vali.save()
        		login(request, user)
        		return redirect('/home/') #render(request, "home.html", { 'form': form })
        	else:
        		return HttpResponse("Usuario Inactivo")
        else:
        	#return redirect('/home/')
        	return render(request, "login.html", { 'form': form })


# Logout
class LogoutView(View):
	def get(self, request):
		user = request.user.pk
		vali = models.login.objects.get(user=user)
		print vali
		vali.activo=False
		vali.save()
		logout(request)
		return render(request, "logout.html")
