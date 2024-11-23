from django.db import models

class AcercaDe(models.Model):
    mision = models.TextField()
    ubicacion = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)

    def __str__(self):
        return "Acerca de nosotros"

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    categoria = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre