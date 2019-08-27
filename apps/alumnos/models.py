from django.db import models

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    poblacion = models.CharField(max_length=40)
    dni = models.CharField(max_length=40)
    fecha_nacimiento = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)