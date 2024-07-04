from django import forms

from .models import Categoria_produtos, Produtos

class formCategoria(forms.ModelForm):

    class Meta:
        model = Categoria_produtos
        fields = ['nome_categoria']
        widgets = {
            'nome_categoria':forms.TextInput(attrs={'class':'class_form'}),
        }

class formProduto(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto',
                  'qtd_produto',
                  'valor_produto',
                  'categoria'
                  ]
                #   'data_vencimento_produto'
                #   'img_produto',
                #   'dono']
        widgets = {
            'nome_produto':forms.TextInput(attrs={'class':'class_form'}),
            'qtd_produto':forms.NumberInput(attrs={'class':'class_form'}),
            'valor_produto':forms.NumberInput(attrs={'class':'class_form'}),
            'categoria':forms.Select(attrs={'class':'class_form'}),
            # 'data_vencimento_produto':forms.DateInput(attrs={'class':'class_form'}),
            # 'img_produto':forms.TextInput(attrs={'class':'class_form'}),
            # 'dono':forms.TextInput(attrs={'class':'class_form'}),
        }