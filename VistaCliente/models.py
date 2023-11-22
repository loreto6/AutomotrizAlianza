from django.db import models
# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.nombre)

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Auto(models.Model):
    imagen= models.ImageField(upload_to='imagenesAutos/')
    modelo = models.CharField(max_length=100)
    valor_inicial = models.FloatField()
    patente = models.CharField(max_length=100,blank=True)
    extras = models.TextField(blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha')

    def __str__(self):
        return str(self.id)

class Publicacion(models.Model):
    precio_venta = models.FloatField()
    disponiblidad= models.CharField(max_length=50, default='Activo') #Activo o Vendido
    id_auto = models.ForeignKey(Auto,on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=200,unique=True)

class Venta(models.Model):
    fecha = models.DateTimeField('Fecha')
    id_publicación = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

class Informe_Compra_Venta(models.Model):
    id_venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    id_auto = models.ForeignKey(Auto,on_delete=models.CASCADE)

#Formularios
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    descripcion = models.TextField()
    id_publicación = models.ForeignKey(Publicacion,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_publicación)