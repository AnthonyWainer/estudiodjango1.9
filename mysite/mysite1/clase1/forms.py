from django import forms
from django.forms import ModelForm
from mysite1.clase1.models import contacto

class formularioContacto(forms.ModelForm):
   def __init__(self, *args, **kwargs):
     super(formularioContacto, self).__init__(*args, **kwargs)
     self.fields['nombre'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'nombre', 'id':'name','required':'',})
     self.fields['email'].widget  = forms.EmailInput(attrs= {'class':'form-control','placeholder':'email', 'id':'email','required':'',})
     self.fields['telefono'].widget= forms.TextInput(attrs= {'class':'form-control','placeholder':'telefono', 'id':'phone','required':'',})
     self.fields['mensaje'].widget= forms.Textarea(attrs= {'class':'form-control','placeholder':'mensaje', 'id':'message','required':'',})
   class Meta:
        model= contacto
