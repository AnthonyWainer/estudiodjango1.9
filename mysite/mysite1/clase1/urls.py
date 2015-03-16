from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('mysite1.clase1.views',
    url(r'^$', index, name="index"),
    url(r'^post/(\d+)$', post),
    url(r'^post2/(\d+)/(\d+)$', post1),
    url(r'^/$', index),
    url(r'^contactenos/$', contactenos,name="contacto"),
    url(r'^acerca/$', acerca,name="acerca"),

)
