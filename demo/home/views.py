from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('menu')
    error = None
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, "home/index.html", {'error': error})

@login_required(login_url='/')
def menu(request):
    return render(request, "home/menu.html")

def cerrar_sesion(request):
    logout(request)
    return redirect('index_view')