from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuarios'  # Esto le dice a Django que use la tabla existente 'usuarios' en la base de datos

    def __str__(self):
        return self.nombre