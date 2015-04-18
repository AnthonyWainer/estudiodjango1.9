from django.contrib import admin
from mysite1.clase1.models import *

# Register your models here.

'''@admin.register(contacto)
class cont(object):
    list_display = ('nombre', 'email')'''
admin.site.register(contacto)