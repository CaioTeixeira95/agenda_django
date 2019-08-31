"""Methods for url's call."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Event


# Create your views here.

def login_user(request):
    """Render the Login Page."""
    return render(request, 'login.html')

def submit_login(request):
    """Verify the login informations from user."""
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
    """Logout the user."""
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def event(request):
    """Insert a new event."""
    return render(request, 'event.html')

def submit_event(request):
    """Save a new event."""
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        Event.objects.create(
            title=title, 
            event_date=event_date, 
            description=description, 
            user=user
        )

    return redirect('/')

# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def event_list(request):
    """List all events."""
    user = request.user
    #event = Event.objects.get(id=1) Pega um determinado registro
    #events = Event.objects.all() # Pega todos os regitro
    events = Event.objects.filter(user=user) # Filtra os resultados de acordo com o parâmetro
    data = {'events': events}
    return render(request, 'agenda.html', data)
