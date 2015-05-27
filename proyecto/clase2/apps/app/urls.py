from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.app.views', 

    #nuestras url de la aplicacion app

    url(r'^hora/$','hora_actual'),
    url(r'^horaAdelante/(\d{1,2})/$','horas_adelante'),
   
    )


