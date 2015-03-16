from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mysite1.clase1.forms import formularioContacto

# Create your views here.
def index(request):
    if request.method == 'POST':
        formulario = formularioContacto(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        formulario = formularioContacto()
    
    return render_to_response('index.html',{'formulario':formulario},context_instance=RequestContext(request))

def contactenos(request):
    return render_to_response('contactenos.html',context_instance=RequestContext(request))

def acerca(request):
    return render_to_response('acerca.html',context_instance=RequestContext(request))

def post(request,p):
    return HttpResponse(p)

def post1(request,p,q):
    html = "hola he retornado por post lo siguiente %s y %s " % (p,q)
    return HttpResponse(html)