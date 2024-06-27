from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('teste', views.teste),
    path('lista_categorias/',views.lista_de_categorias_view),
    path('cadastrar_categorias/',views.cadastrar_categoria),
]