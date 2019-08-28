from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from apps.alumnos.models import Alumno
from apps.alumnos.forms import AlumnoForm

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

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

class ReporteAlumnosPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE ALUMNOS")

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
        encabezado = ('Nombre', 'Apellido', 'Direccion', 'DNI', 'Fecha de nacimiento', 'Telefono')
        detalle = [(alumno.nombre, alumno.apellido, alumno.direccion, alumno.dni, alumno.fecha_nacimiento. alumno.telefono) for alumno in Alumno.objects.all()]
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







