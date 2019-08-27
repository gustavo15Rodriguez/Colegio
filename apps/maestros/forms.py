from django import forms
from apps.maestros.models import Profesor, Aula, Asignatura, Curso

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'poblacion': 'Poblacion',
            'dni': 'Dni',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'codigo_postal': 'Codigo Postal',
            'telefono': 'Telefono',
        }

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-cotrol'})



class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula

        fields = "__all__"

        labels = {
            'piso':'Piso',
            'numero_pupitres':'Numero Pupitres',
            'asignaturas': 'Asignaturas',
        }

    def __init__(self, *args, **kwargs):
        super(AulaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})




class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura

        fields = "__all__"

        labels = {
            'nombre':'Nombre',
            'numero_horas':'Numero De Horas',
            'nota': 'Nota',
            'incidencias': 'Incidencias',
            'alumnos': 'Alumno',
        }

    def __init__(self, *args, **kwargs):
        super(AsignaturaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'asignaturas': 'Asignaturas',
            'tutor': 'Tutor',
        }

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})