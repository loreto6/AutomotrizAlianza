from django.urls import path,include
from . import views


app_name = 'automotrizz'

urlpatterns=[
    path('',views.PublicacionesViewCliente,name='home'), #Las publicaciones (sin permisos)
    path('Auto/<int:id>/',views.DetallesPublicaciones,name='publicacion_detalle'), #Detalles que los clientes pueden ver desde home (sin permisos)
    path('PanelAdmin/',views.ViewAdmin,name='index_admin'), #Para ingresar, primero tiene que logearse
    path('accounts/',include('django.contrib.auth.urls')),#Sistema de logeo
    path('exit/',views.exit,name='exit'),#Sistema de logout
    path('AddAuto/',views.AddAdminAuto,name='registrarauto'), #Registar los autos en la BD (con permisos)
    path('ViewAutos/',views.ViewAdminAuto,name='AutosRegistrados'), #Lista de Autos registrados (con permisos)
    path('PublicaciónAuto/<int:id>/',views.publicar_auto,name='publicar_auto'),#Realiza la publicacion pidiendo el monto con el que se va a publicar (con permisos)
    path('DeleteAuto/<int:id>/',views.DeleteAuto,name='eliminarAuto'),# Elimina el auto de la BD (con permisos)
    path('DeletePublicacion/<int:id>/',views.DeletePublicacion,name='eliminarPublicacion'),#Elimina la publicacion (con permisos)
    path('AutoDetalle/<int:pk>/',views.DetalleAuto,name='auto_detalle'),#Informacion de los autos registrados (con permisos)
    path('ListadoPubli/',views.ViewPublicacion,name='listado_publicacion'),#Lista de publicaciones activas (con permisos)
    path('ChangePublicacion/<int:id>/',views.ChangePublicacion,name='changePublicacion'), #Modificar las publicaciones (con permisos)
    path('ChangeAuto/<int:id>/',views.ChangeAuto,name='changeAuto'),#Modificar la informacion de los autos (con permisos)
    path('Contactos/',views.ViewContacto,name='ViewContacto'),
    path('ReporteCompra/', views.ViewReporteCompra, name='ViewReporteCompra'),
    path('Venta/',views.RealizarVenta.AddVenta,name='RealizarVenta'),
]