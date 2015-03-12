from django.db import models

# Create your models here.

class perfil(models.Model):
    descripcion = models.CharField(max_length=50)
    estado      = models.BooleanField(default=True)

class accesos(models.Model):
    idperfil = models.ForeignKey(perfil)
    estado   = models.BooleanField(default=True)