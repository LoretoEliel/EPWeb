"""settings URL Configuration

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
from contenido.views import LibroDetailView, LibroUpdateView
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #ESTO ES EL SISTEMA LOGIN
    url(r'^$', login,
        {'template_name': 'index.html'},
        name="login"),
    url(r'^logout/$', logout,
        {'template_name': 'logout.html'}),

    #ESTO ES PARA RECUPERAR MI CUENTA CUANDO OLVIDO LA CLAVE
    #!IMPORTANT --------------------------------------------
    url(r'^reset/password_reset', password_reset,
        {'template_name':'reset_password/password_reset_form.html',
        'email_template_name':'reset_password/password_reset_email.html'},
        name='password_reset'),
    url(r'^reset/password_reset_done', password_reset_done,
        {'template_name':'reset_password/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name':'reset_password/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^reset/completado', password_reset_complete,
        {'template_name':'reset_password/password_reset_complete.html'},
        name="password_reset_complete"),
    # ------------------------------------------------------

    #NUEVOS USUARIOS
    url(r'^add_user/$', 'acounts.views.add_user', name='add_user'),
    url(r'^success/$', 'acounts.views.register_success'),

    #HOME O DENTRO DEL SISTEMA
    url(r'^home/$', 'contenido.views.home', name="Home"),
        url(r'^libro/(?P<slug>[-\w]+)/$', LibroDetailView.as_view()),
        url(r'^update/(?P<slug>[-\w]+)/$', LibroUpdateView.as_view(), name="actualizando"),
        url(r'^mi_perfil/$', 'acounts.views.my_perfil', name="MyPerfil"),

    #CONTACTAME
    #url(r'^contacto/$', ContactFormView.as_view(), name='contacto'),
    url(r'^contacto/$', 'acounts.views.contacto_email', name="Contacto"),
        url(r'^email_envidado/$', 'acounts.views.contacto_exitoso', name="Contacto_Exitoso"),

    #ESTO ES PARA AGREGAR CONTENIDO AL BLOG
    url(r'^agregar_libro/$', 'contenido.views.UploadLibro', name="Libros"),
        url(r'^libro_guardado/$', 'contenido.views.libro_guardado', name="Libro_Guardado"),
        url(r'^mis_libros/$', 'contenido.views.MisLibros', name="MisLibros"),
        url(r'^info/(?P<pk>\d+)/eliminar/$', 'contenido.views.Eliminar_libro', name='eliminar_libro'),

    #FORO DEL SITIO
    url(r'^foro/$', 'foro.views.chatbox', name='messenger'),
    url(r'^post/$', 'foro.views.Post', name='post'),
    url(r'^messages/$', 'foro.views.Messages', name='messages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
