from django import forms
from django.contrib.auth.forms import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__' traz todas as especificações dos usuários
        fields = ['username',
        'password']
        label = {
            'password': 'Senha',
            'username': 'Usuario'
        }
