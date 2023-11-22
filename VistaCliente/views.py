from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .forms import *
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# Create your views here.
def PublicacionesViewCliente(request): #Las publicaciones que pueden ver los clientes
    tarjeta=Publicacion.objects.all()
    context={'tarjeta':tarjeta}
    return render(request,'PublicacionViewCliente.html',context)

def DetallesPublicaciones(request,id):#Detalle de publicaciones que ven los clientes (incluido el formulario de contacto)
    detalle = Publicacion.objects.get(id = id)
    context1 = {'detalle':detalle}
    data = {'form':ContactoForm()}
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        formulario = formulario.save(commit=False)
        formulario.id_publicación = detalle
        formulario.save()
        data['mensaje']='Contacto Enviado'
    context = {**context1,**data}
    return render (request,'PublicacionDetalle.html',context)

def ViewContacto(request):
    contactos = Contacto.objects.all()
    context={'contactos':contactos}
    return render(request,'ViewContacto.html',context)

@login_required
def ViewAdmin(request):
    user = request.user
    context = {'user':user}
    return render (request,'index_admin.html',context)

def exit(request):
    logout(request)
    return redirect('/')

#!CRUD RESPORTES--------------------------------------------
def ViewReporteCompra(request):
    registro = Auto.objects.all()
    data = {'registro':registro}
    return render(request,"Reporte.html",data)
#!----------------------------------------------------------

#?CRUD Venta-------------------------------------------------
class RealizarVenta(HttpResponse):
    def AddVenta(request):
        data={'FormVenta':FormVenta()}
        if request.method=='POST':
            formulario = FormVenta(request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,'AddVenta.html',data)
        
#?----------------------------------------------------------

#CRUD autos-------------------------------------------------
def ViewAdminAuto(request): #Ver listados de autos ya registrados
    auto = Auto.objects.all()
    data1={'autos':auto}
    
    

            
    data = {**data1}
    return render(request,'CRUDauto.html',data)

def DetalleAuto(request,pk): #ver detalles de los autos ya registrados
    detalle = Auto.objects.get(pk = pk)
    context = {'detalle':detalle}
    return render (request,'auto_detalle.html',context)

def AddAdminAuto(request):
    auto = RegistarAuto()
    data ={'FormCar':RegistarAuto()}
    if request.method == 'POST':
        auto = RegistarAuto(request.POST, request.FILES)
        if auto.is_valid():
            auto.save()
            data['mensaje'] = 'AUTOMOVIL GUARDADO EXITOSAMENTE'
    return render(request,'AddAuto.html',data)

def ChangeAuto(request,id):
    auto = Auto.objects.get(id=id)
    data = {'changeform':RegistarAuto(instance=auto)}
    if request.method == 'POST':
        form = RegistarAuto(data=request.POST,instance=auto)
        if form.is_valid():
            form.save()
            return redirect('automotrizz:AutosRegistrados')
        data['form'] = form
    return render(request,'change.html',data)


def DeleteAuto(request, id): #Eliminar un auto de la base de datos
    auto = Auto.objects.get(id=id)
    if request.method == 'POST': #Confirmación de eliminación
        auto.delete()
        return redirect('automotrizz:AutosRegistrados')
    return render(request, 'confirm_delete.html', {'id': id})
#----------------------------------------------------------------


# CRUD de publicación--------------------------------------------
def ViewPublicacion(reques):
    publ = Publicacion.objects.all()
    data = {'ViewPubli':publ}
    return render (reques,'ListadoPublicacion.html',data)

def publicar_auto(request, id): 
    auto = Auto.objects.get(id=id)
    data = {'FormPubli':FormPublicacion()}
    if request.method=='POST':
        formulario = FormPublicacion(data=request.POST)
        formulario = formulario.save(commit=False)
        formulario.id_auto = auto
        formulario.save()
        data['mensaje']='Publicación Exitosa'
    return render (request,'AddPublicacion.html',data)

def ChangePublicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)
    data = {'changeform':FormPublicacion(instance=publicacion)}
    if request.method == 'POST':
        form = FormPublicacion(data=request.POST,instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('automotrizz:listado_publicacion')
        data['changeform'] = form
    return render(request,'change.html',data)

def DeletePublicacion(request, id): #Eliminar una publicacion
    publi = Publicacion.objects.get(id=id)
    if request.method == 'POST': #Confirmación de eliminación
        publi.delete()
        return redirect('automotrizz:listado_publicacion')
    return render(request, 'confirm_delete.html', {'id': id})
#-----------------------------------------------------------------


