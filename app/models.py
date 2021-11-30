from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.tipo
        

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    oferta = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

opciones_pago = [
    [0, "Debito"],
    [1, "Credito"],
    [2, "Transferencia"],
]

opciones_aviso = [
    [0, "Disponible en Estacion Baquedano"],
    [1, "Disponible en Los Dominicos"],
]

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_pago = models.IntegerField(choices=opciones_pago)
    avisos = models.IntegerField(choices=opciones_aviso)
    monto_donacion = models.IntegerField()

    def __str__(self):
        return self.nombre
