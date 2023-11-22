from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = {'nombre','correo','descripcion'}
        
class RegistarAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields= '__all__'
        widgets = {'fecha':forms.DateInput(attrs={'type':'date'})}

class FormPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['precio_venta']

class FormVenta(forms.ModelForm):
    class Meta:
        model = Venta
        fields ='__all__'
        widgets = {'fecha':forms.DateInput(attrs={'type':'date'})}

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'