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
