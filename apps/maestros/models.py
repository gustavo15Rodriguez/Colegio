from django.db import models
from apps.alumnos.models import Alumno

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    poblacion = models.CharField(max_length=40)
    dni = models.CharField(max_length=40)
    fecha_nacimiento = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    numero_horas = models.IntegerField()
    nota = models.CharField(max_length=40)
    incidencias = models.CharField(max_length=60)
    alumnos = models.ForeignKey(Alumno, on_delete=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    asignaturas = models.ForeignKey(Asignatura, on_delete=True, blank=True, null=True)
    tutor = models.ForeignKey(Profesor, on_delete=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Aula(models.Model):
    id_aula = models.AutoField(primary_key=True)
    piso = models.IntegerField()
    numero_pupitres = models.IntegerField()
    asignaturas = models.ForeignKey(Asignatura, on_delete=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.piso)
