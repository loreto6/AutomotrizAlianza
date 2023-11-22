from django.contrib import admin
from .models import Marca, Year, Auto, Publicacion, Cliente, Venta, Informe_Compra_Venta, Contacto

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class YearAdmin(admin.ModelAdmin):
    list_display = ['year']

class AutoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'year', 'marca']

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','descripcion','id_publicación']

# Register your models here.
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Year,YearAdmin)
admin.site.register(Auto,AutoAdmin)
admin.site.register(Publicacion)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Informe_Compra_Venta)
admin.site.register(Contacto,ContactoAdmin)