from django.db import models

# Create your models here.

class perfil(models.Model):
    descripcion = models.CharField(max_length=50)
    estado      = models.BooleanField(default=True)

class accesos(models.Model):
    idperfil = models.ForeignKey(perfil)
    estado   = models.BooleanField(default=True)

class contacto(models.Model):
    nombre   = models.CharField(max_length=50)
    email    = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mensaje  = models.CharField(max_length=100)

class Document(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')