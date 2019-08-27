from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.alumnos.models import Alumno
from apps.alumnos.forms import AlumnoForm

class CreateAlumno(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/alumno_form.html'
    success_url = reverse_lazy('listar_alumnos')

class UpdateAlumno(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/alumno_form.html'
    success_url = reverse_lazy('listar_alumnos')


class DeleteAlumno(DeleteView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/alumno_delete.html'
    success_url = reverse_lazy('listar_alumnos')


class ListAlumno(ListView):
    model = Alumno
    template_name = 'alumno/alumno_list.html'







