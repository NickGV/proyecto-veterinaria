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

class Menu(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    servCaninos = models.CharField(max_length=255)
    servFelinos = models.CharField(max_length=255)
    testimonios = models.CharField(max_length=255)
    
    def __str__(self):
        return "Menu Principal"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    categoria = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.EmailField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    catalogo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.cantidad} unidades de {self.producto.nombre} de {self.proveedor.nombre}"