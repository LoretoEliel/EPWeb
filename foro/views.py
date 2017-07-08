from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from settings import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Chat
from .forms import ChatForm

from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


@login_required()
def chatbox(request):
    c = Chat.objects.all()
    queryset_list = User.objects.all()
    Page_reques_var = "page"
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(titulo__icontains=query)|
            Q(subida__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 1000)
    Page_reques_var = "page"
    page = request.GET.get(Page_reques_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            newdoc = Chat(mensaje = request.POST['mensaje'],
                user = request.user)
            newdoc.save(form)
            return redirect("messenger")
    else:
        form = ChatForm()

    ctx = {
        'object_list':queryset,
        'username': 'List',
        'last_login_1': 'List',
        'messenger': 'active',
        'chat': c,
        'form': form
    }

    return render(request, "foro.html", ctx)

@login_required()
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

@login_required()
def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})
