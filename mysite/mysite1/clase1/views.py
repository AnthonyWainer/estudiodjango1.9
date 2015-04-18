#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mysite1.clase1.forms import formularioContacto, formularioLogin,UploadForm
from mysite1.clase1.models import contacto, Document
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        formulario = formularioContacto(request.POST)

        if formulario.is_valid():
            a= contacto()
            a.nombre   = formulario.cleaned_data['nombre']
            a.email    = formulario.cleaned_data['email']
            a.telefono = formulario.cleaned_data['telefono']
            a.mensaje  = formulario.cleaned_data['mensaje']
            a.save()
            return HttpResponseRedirect('/')
    else:
        formulario = formularioContacto()
    
    return render_to_response('index.html',{'formulario':formulario},context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        formulario = formularioLogin(request.POST)

        if formulario.is_valid():
            usuario  = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['password']

            user = auth.authenticate(username=usuario, password=password)

            if user is not None  and user.is_active:
                auth.login(request, user)
                return HttpResponse("ha ingresado con éxito")
            else: 
                msm= "usuario y clave son incorrectos"  
        else:
            msm = "DATOS INCORRECTOS"
        login = formularioLogin()
        return render_to_response('login.html',{'login':login,'msm':msm},context_instance=RequestContext(request))
    else:
        login = formularioLogin()
        return render_to_response('login.html',{'login':login,'msm':''},context_instance=RequestContext(request))        

def acerca(request):
    return render_to_response('acerca.html',context_instance=RequestContext(request))

def post(request,p):
    return HttpResponse(p)

def post1(request,p,q):
    html = "hola he retornado por post lo siguiente %s y %s " % (p,q)
    return HttpResponse(html)

import csv
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        #ass = request.FILES['docfile'].open("rb")
        #reader = csv.reader(request.FILES['docfile'].file)
        reader = csv.DictReader(request.FILES['docfile'].file) #serializar para base datos
        #print reader
        a= []
        for i in reader:
            a.append(i)

        #print a[0]
        return HttpResponse(a[1])
        #cs(ass)
        
        if form.is_valid():
            newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
            #newdoc.save(form)
            #return HttpResponseRedirect(ass)
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    #return render(request, 'upload.html', {'form': form})



