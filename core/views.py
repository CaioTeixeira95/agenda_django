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
    id_event = request.GET.get('id')
    data = {}
    if id_event:
        data['event'] = Event.objects.get(id=id_event)

    return render(request, 'event.html', data)

def submit_event(request):
    """Save a new event."""
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        local = request.POST.get('local')
        user = request.user

        id_event = request.POST.get('id_event')

        if id_event:
            event = Event.objects.get(id=id_event)
            if event.user == user:
                event.title = title
                event.event_date = event_date
                event.description = description
                event.local = local
                event.save()
        else:
            Event.objects.create(
                title=title, 
                event_date=event_date, 
                description=description,
                local=local,
                user=user
            )

    return redirect('/')

@login_required()
def delete_event(request, id_event):
    """Delete an event."""
    user = request.user
    event = Event.objects.get(id=id_event, user=user)
    
    if user == event.user:
        event.delete()

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
