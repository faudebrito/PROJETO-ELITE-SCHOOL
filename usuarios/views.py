from django.shortcuts import render
from .form import UsuarioForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registrar_usuario(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()

            usuario_cadastrado = authenticate(username = novo_usuario.username, password = request.POST['password1'])
    else:
        form = UserCreationForm()

    contexto = {'form':form}
    return render(request,'registro_usuario.html',contexto)



