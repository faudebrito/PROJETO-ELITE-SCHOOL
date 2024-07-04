from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home),
    path('lista_categoria/',views.lista_de_categoria_view),
    path('lista_de_produto/',views.lista_de_produto_view),
    path('cadastrar_categoria/',views.cadastrar_categoria),
    path('cadastrar_produto/',views.cadastrar_categoria),
]