from apps.maestros.views import DeleteAsignatura,UpdateAsignatura,CreateAsignatura,ListAsignatura,CreateProfesor,DeleteProfesor, ReporteAsignaturaPDF, ReporteAulaPDF, ReporteCursoPDF, ReporteProfesorPDF
from apps.maestros.views import UpdateProfesor, ListProfesor,CreateCurso, DeleteCurso, UpdateCurso, ListCurso, CreateAula, ListAula, DeleteAula, UpdateAula
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^profesor/listar$', login_required(ListProfesor.as_view()), name='profesor_listar'),
    url(r'^profesor/crear$', login_required(CreateProfesor.as_view()), name='profesor_crear'),
    url(r'^profesor/editar/(?P<pk>[\d]+)/$', login_required(UpdateProfesor.as_view()), name='profesor_editar'),
    url(r'^profesor/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteProfesor.as_view()), name='profesor_eliminar'),
    url(r'^asignatura/listar$', login_required(ListAsignatura.as_view()), name='asignatura_listar'),
    url(r'^asignatura/crear$', login_required(CreateAsignatura.as_view()), name='asignatura_crear'),
    url(r'^asignatura/editar/(?P<pk>[\d]+)/$', login_required(UpdateAsignatura.as_view()), name='asignatura_editar'),
    url(r'^asignatura/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteAsignatura.as_view()), name='asignatura_eliminar'),
    url(r'^asignatura/listar$', login_required(ListAsignatura.as_view()), name='asignatura_listar'),
    url(r'^curso/crear$', login_required(CreateCurso.as_view()), name='curso_crear'),
    url(r'^curso/listar$', login_required(ListCurso.as_view()), name='curso_listar'),
    url(r'^curso/editar/(?P<pk>[\d]+)/$', login_required(UpdateCurso.as_view()), name='curso_editar'),
    url(r'^curso/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteCurso.as_view()), name='curso_eliminar'),
    url(r'^aula/crear$', login_required(CreateAula.as_view()), name='aula_crear'),
    url(r'^aula/listar$', login_required(ListAula.as_view()), name='aula_listar'),
    url(r'^aula/editar/(?P<pk>[\d]+)/$', login_required(UpdateAula.as_view()), name='aula_editar'),
    url(r'^aula/eliminar/(?P<pk>[\d]+)/$', login_required(DeleteAula.as_view()), name='aula_eliminar'),

    url(r'^profesor/reporte_profesor_pdf/', login_required(ReporteProfesorPDF.as_view()), name='reporte_profesor_pdf'),
    url(r'^profesor/reporte_aula_pdf/', login_required(ReporteAulaPDF.as_view()), name='reporte_aula_pdf'),
    url(r'^profesor/reporte_asignatura_pdf/', login_required(ReporteAsignaturaPDF.as_view()), name='reporte_asignatura_pdf'),
    url(r'^profesor/reporte_curso_pdf/', login_required(ReporteCursoPDF.as_view()), name='reporte_curso_pdf'),
]
