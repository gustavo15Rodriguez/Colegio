from django.conf.urls import url
from apps.alumnos.views import CreateAlumno, UpdateAlumno, DeleteAlumno, ListAlumno
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^alumno/listar$', login_required(ListAlumno.as_view()), name='alumno_listar'),
    url(r'^alumno/crear$', login_required(CreateAlumno.as_view()), name='alumno_crear'),
    url(r'^alumno/editar/(?P<pk>[\d]+)/$', login_required(UpdateAlumno.as_view()), name='alumno_editar'),
    url(r'^alumno/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteAlumno.as_view()), name='alumno_eliminar'),
]