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
        fields = "__all__" 

class formularioLogin(forms.Form):
    usuario  = forms.CharField(widget= forms.TextInput(attrs={'class':"form-control", 'placeholder':"Usuario", 'required':'', 'autofocus':''}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'type':"password", 'id':"inputPassword", 'class':"form-control", 'placeholder':"Password", 'required':''}))
    def clean(self):
        return self.cleaned_data

class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100)
    docfile = forms.FileField(
        label='Selecciona un archivo'
    )