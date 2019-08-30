from django.shortcuts import render, HttpResponse, redirect
from core.models import Event

# Create your views here.

def events(request, title):
    res = Event.objects.get(title=title)
    return HttpResponse("The local of the event is: {}".format(res.local))

# def index(request):
#     return redirect('/agenda/')

def event_list(request):
    user = request.user
    #event = Event.objects.get(id=1) Pega um determinado registro
    events = Event.objects.all() # Pega todos os regitro
    #events = Event.objects.filter(user=user) # Filtra os resultados de acordo com o parâmetro
    data = {'events': events}
    return render(request, 'agenda.html', data)
