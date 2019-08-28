from django import forms
from apps.alumnos.models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = "__all__"

        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'direccion':'Direccion',
            'poblacion':'Poblacion',
            'dni':'Dni',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'codigo_postal':'Codigo Postal',
            'telefono':'Telefono',
        }

    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


