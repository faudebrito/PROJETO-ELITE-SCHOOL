from django.shortcuts import render

from django.http import HttpResponse

def index(requests):
    return render(requests, 'gerenciador_school/index.html')
def teste(requests):
    return render(requests, 'teste.html')

# def home(request):
#     return render(request,'manager_marketplace/paginas/home.html')