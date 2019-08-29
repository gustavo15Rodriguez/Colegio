from apps.maestros.models import Profesor, Asignatura, Aula, Curso
from apps.maestros.forms import AsignaturaForm, AulaForm, CursoForm, ProfesorForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View
from django.urls import reverse_lazy

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import TableStyle, Table
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReporteProfesorPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE PROFESORES")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('Nombre', 'Apellido', 'Direccion', 'DNI', 'F. nacimiento', 'Telefono')
        detalle = [(profesor.nombre, profesor.apellido, profesor.direccion, profesor.dni, profesor.fecha_nacimiento, profesor.telefono) for profesor in Profesor.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[3 * cm, 3 * cm, 3 * cm, 3 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


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
    template_name = 'profesor/profesor_eliminar.html'
    success_url = reverse_lazy('profesor_listar')


class ListProfesor(ListView):
    model = Profesor
    template_name = 'profesor/profesor_listar.html'

#---------------------------Asignatura---------------------------------

class ReporteAsignaturaPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE ASIGNATURAS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('ID', 'Nombre', 'Num. horas', 'Nota', 'Incidencias', 'Alumnos')
        detalle = [(asignatura.id_asignatura, asignatura.nombre, asignatura.numero_horas, asignatura.nota, asignatura.incidencias, asignatura.alumnos) for asignatura in Asignatura.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[3 * cm, 3 * cm, 3 * cm, 3 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

class CreateAsignatura(CreateView):
    model = Profesor
    form_class = AsignaturaForm
    template_name = 'asignatura/asignatura_form.html'
    success_url = reverse_lazy('asignatura_listar')


class UpdateAsignatura(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'asignatura/asignatura_form.html'
    success_url = reverse_lazy('asignatura_listar')


class DeleteAsignatura(DeleteView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'asignatura/asignatura_eliminar.html'
    success_url = reverse_lazy('asignatura_listar')


class ListAsignatura(ListView):
    model = Asignatura
    template_name = 'asignatura/asignatura_listar.html'


#---------------------------Aula---------------------------------

class ReporteAulaPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE AULAS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('ID', 'Piso', 'Numero de pupitres', 'Asignaturas')
        detalle = [(aula.id_aula, aula.piso, aula.numero_pupitres, aula.asignaturas) for aula in Aula.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class CreateAula(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula_listar')


class UpdateAula(UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula_listar')


class DeleteAula(DeleteView):
    model = Aula
    form_class = AulaForm
    template_name = 'aula/aula_eliminar.html'
    success_url = reverse_lazy('aula_listar')


class ListAula(ListView):
    model = Aula
    template_name = 'aula/aula_listar.html'


#---------------------------Curso---------------------------------

class ReporteCursoPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE CURSOS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('ID', 'Nombre', 'Asignaturas', 'Tutor')
        detalle = [(curso.id_curso, curso.nombre, curso.asignaturas, curso.tutor) for curso in Curso.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class CreateCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('curso_listar')


class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('curso_listar')


class DeleteCurso(DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_eliminar.html'
    success_url = reverse_lazy('curso_listar')


class ListCurso(ListView):
    model = Curso
    template_name = 'curso/curso_listar.html'
