from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Email',
            'username': 'Username',
        }

    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombres'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellidos'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input-text'})