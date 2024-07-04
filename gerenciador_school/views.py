from django.shortcuts import render

from django.http import HttpResponse

from .models import Categoria_produtos, Produtos

from .forms import formCategoria, formProduto

def index(requests):
    return render(requests, 'gerenciador_school/index.html')
def home(request):
    return render(request,'gerenciador_school/home.html')

def lista_de_categoria_view(request):

    lista_categorias = Categoria_produtos.objects.all()

    contexto = {'categorias':lista_categorias}

    return render(request,'gerenciador_school/lista_de_categorias.html',contexto)

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = formCategoria(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Cadastrado com sucesso')
    else:
        form = formCategoria()
    
    contexto = {'form':form}

    return render(request,'gerenciador_school/cadastrar_categoria.html',{'form':form})   

def cadastrar_produto(request):
    if request.method == 'POST':
        form = formProduto(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Cadastrado com sucesso')
    else:
        form = formProduto()
    
    contexto = {'form':form}

    return render(request,'gerenciador_school/cadastrar_produto.html',contexto)   

def lista_de_produto_view(request):

    produtos = Produtos.objects.all()

    contexto = {'produto':produtos}

    return render(request,'gerenciador_school/lista_de_produto.html',contexto)