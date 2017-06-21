"""ElProgramadorWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings 
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from contenido import views

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #ESTO ES EL SISTEMA LOGIN
    url(r'^login/$', login, {'template_name': 'login.html' }, name="login"),
    url(r'^logout/$', logout, {'template_name': 'logout.html', }),

    #NUEVOS USUARIOS
    url(r'^add_user/$', 'acounts.views.add_user', name='add_user'),
    url(r'^success/$', 'acounts.views.register_success'),

    #FRONT INICIAL
    url(r'^$', 'contenido.views.index', name="Index"),

    #HOME O DENTRO DEL SISTEMA
    url(r'^home/$', 'contenido.views.home', name="Home"),
        url(r'^mi_perfil/$', 'acounts.views.my_perfil', name="MyPerfil"),

    #CONTACTAME
    #url(r'^contacto/$', ContactFormView.as_view(), name='contacto'),
    url(r'^contacto/$', 'acounts.views.contacto_email', name="Contacto"),
        url(r'^email_envidado/$', 'acounts.views.contacto_exitoso', name="Contacto_Exitoso"),

    #ESTO ES PARA AGREGAR CONTENIDO AL BLOG
    url(r'^agregar_info/$', 'contenido.views.info', name="Informacion"),
        url(r'^info_guardada/$', 'contenido.views.info_guardada'),
        url(r'^info/(?P<pk>\d+)/eliminar/$', views.eliminar_info, name='eliminar_info'),

    #FORO DEL SITIO
    url(r'^foro/$', 'foro.views.chatbox', name='messenger'),
    url(r'^post/$', 'foro.views.Post', name='post'),
    url(r'^messages/$', 'foro.views.Messages', name='messages'),

    #REPRODUCTOR DE MUSICA
    url(r'^Index_musica/$', 'CMPlayList.views.index_music', name="Index_Music"),
        url(r'^agregar_musica/$', 'CMPlayList.views.Agregar_Musica', name="Add_musica"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)