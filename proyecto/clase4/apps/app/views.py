from django.shortcuts import render, render_to_response
from datetime import datetime
import datetime

# Crea tus vistas aqui.

def hora_actual(request):
    hora = datetime.now()
    return render_to_response('app/hora.html',{'hora':hora})

def horas_adelantada(request, hora):
    try:
        horas = int(hora)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = horas)
    return render(request,"app/horas_adelante.html",{'hora_siguiente':dt, 'horas':horas})

def marlon(request):
    marlon = "html='hola soy nuevo en Django'"
    marlon1 = "nombre='marlon'"
    return render_to_response('app/marlon.html',{'html':marlon,'html1':marlon1})
    