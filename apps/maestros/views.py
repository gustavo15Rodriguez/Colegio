from apps.maestros.models import Profesor, Asignatura, Aula, Curso
from apps.maestros.forms import AsignaturaForm, AulaForm, CursoForm, ProfesorForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

class CreateProfesor(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor_listar')


class UpdateProfesor(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor_listar')

class DeleteProfesor(DeleteView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_delete.html'
    success_url = reverse_lazy('profesor_listar')


class ListProfesor(ListView):
    model = Profesor
    template_name = 'profesor/profesor_list.html'


#---------------------------Asignatura---------------------------------

class CreateAsignatura(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor_listar')


class UpdateAsignatura(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'profesor/asignatura_form.html'
    success_url = reverse_lazy('asignatura_listar')


class DeleteAsignatura(DeleteView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'profesor/asignatura_delete.html'
    success_url = reverse_lazy('asignatura_listar')


class ListAsignatura(ListView):
    model = Asignatura
    template_name = 'profesor/asignatura_list.html'


#---------------------------Aula---------------------------------

class CreateAula(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'profesor/aula_form.html'
    success_url = reverse_lazy('aula_listar')


class UpdateAula(UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'profesor/aula_form.html'
    success_url = reverse_lazy('aula_listar')


class DeleteAula(DeleteView):
    model = Aula
    form_class = AulaForm
    template_name = 'profesor/aula_delete.html'
    success_url = reverse_lazy('aula_listar')


class ListAula(ListView):
    model = Aula
    template_name = 'profesor/aula_list.html'


#---------------------------Curso---------------------------------

class CreateCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'profesor/curso_form.html'
    success_url = reverse_lazy('curso_listar')


class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'profesor/curso_form.html'
    success_url = reverse_lazy('curso_listar')


class DeleteCurso(DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'profesor/curso_delete.html'
    success_url = reverse_lazy('curso_listar')


class ListCurso(ListView):
    model = Curso
    template_name = 'profesor/curso_list.html'
