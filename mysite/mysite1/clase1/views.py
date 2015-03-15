from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def contactenos(request):
    return render_to_response('contactenos.html',context_instance=RequestContext(request))

def acerca(request):
    return render_to_response('acerca.html',context_instance=RequestContext(request))

def post(request,p):
    return HttpResponse(p)

def post1(request,p,q):
    html = "hola he retornado por post lo siguiente %s y %s " % (p,q)
    return HttpResponse(html)