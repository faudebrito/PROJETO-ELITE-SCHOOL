from django import forms

from .models import Categoria_produtos

class formCategoria(forms.ModelForm):

    class Meta:
        model = Categoria_produtos
        fields = ['nome_categoria']
        widgets = {
            'nome_categoria':forms.TextInput(attrs={'class':'class_form'}),
        }
