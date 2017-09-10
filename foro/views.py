from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from settings import settings

from django.contrib.auth.models import User
from .models import Chat
from .forms import ChatForm
from acounts import models

from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

#JySa 
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
######

class Chatbox(ListView):
    model = User
    second_model = models.login
    template_name = "foro.html"

    def get_context_data(self, **kwargs):
        context = super(Chatbox, self).get_context_data(**kwargs)
        context['chat'] = Chat.objects.all()
        ga = Chat.objects.all().order_by('-id')
        lista = []
        for i in ga:
            lista.append(i.id)
        if len(lista)!=0:
            context['aja'] = max(lista)
        else:
            context['aja'] = 0 
        return context


# Aqui se aplico Json
class Verificar(TemplateView):
    model = models.login
    second_model = User

    def get(self, request, *args, **kwargs):
        ver = self.model.objects.all().order_by('-id')
        data = {}
        acu = 0
        for i in ver:
            user = self.second_model.objects.get(pk=str(i.user.id)) 
            data[acu]={
                        'id':user.pk, 'username':user.username,
                        'first_name':user.first_name, 'last_name':user.last_name,
                        'email':user.email, 'last_login':user.last_login,
                        'activo':i.activo,
                    }
            acu += 1
        return JsonResponse(data)

class CreateBox(CreateView):
    model = Chat
    form_class = ChatForm

    def post(self, request, *args, **kwargs):
        valor = request.POST.get("ced")
        data = {}
        if valor:
            mensa = self.model(user=request.user, mensaje=valor)
            mensa.save()
            data= {'validar':True, 'ver':{'message':valor,
                                    'user':mensa.user.username,
                                    'enviado':mensa.enviado,
                                    },}  
        else:
            data= {'validar':False}  
        return JsonResponse(data)

class Messages(TemplateView):
    def get(self, request, *args, **kwargs):
        data ={'validar':None, 'acu':None}
        acu = 0
        acum = 0
        aj =  request.GET["id"]
        ga = Chat.objects.raw('SELECT  *  FROM foro_chat where id > %s' % (str(aj)))
        for i in ga:
            acum += 1
        if acum != 0:
            data = {'validar':True}
            for i in ga:
                data[acu]={'user':i.user.username, 'mesage':i.mensaje, 'enviado':i.enviado 
                }
                acu +=1
        else:
            data= {'validar':False}
        return JsonResponse(data)