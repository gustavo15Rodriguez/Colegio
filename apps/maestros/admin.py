from django.contrib import admin
from apps.maestros.models import Profesor
from apps.maestros.models import Asignatura
from apps.maestros.models import Aula
from apps.maestros.models import Curso

admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Aula)
admin.site.register(Curso)
