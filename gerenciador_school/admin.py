from django.contrib import admin
from .models import Categoria_produtos,Produtos

# Register your models here.
@admin.register(Categoria_produtos)
class AdminProdutos(admin.ModelAdmin):
    ...

@admin.register(Produtos)
class AdminCategoria_produtos(admin.ModelAdmin):
    ...

# admin.site.register(Categoria_produtos, AdminCategoria_produtos)