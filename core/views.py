from django.shortcuts import render, HttpResponse, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):

    if request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Usuário e/ou senha inválido')
    
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def events(request, title):
    res = Event.objects.get(title=title)
    return HttpResponse("The local of the event is: {}".format(res.local))

# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def event_list(request):
    user = request.user
    #event = Event.objects.get(id=1) Pega um determinado registro
    #events = Event.objects.all() # Pega todos os regitro
    events = Event.objects.filter(user=user) # Filtra os resultados de acordo com o parâmetro
    data = {'events': events}
    return render(request, 'agenda.html', data)
