from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def hospedaje(request):
    return render(request, "home/hospedaje.html")
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

    razas_gatos = [
        "Siamés", "Persa", "Maine Coon", "Bengala", "Sphynx", "Ragdoll", "British Shorthair", "Abisinio", "Escocés", "Noruego"
    ]

    razas_perro = [
        "Chihuahua", "Pug", "Pastor Alemán", "Labrador", "Golden Retriever", "Bulldog", "Beagle", "Dálmata", "Boxer", "Shih Tzu", "Pomerania", "Pitbull", "Schnauzer", "Doberman", "Rottweiler", "Cocker Spaniel", "Border Collie", "Husky", "Samoyedo", "Akita"
    ]
    mascota = {}
    if request.method == "POST":
        mascota["id"] = request.POST.get("id_mascota")
        mascota["nombre"] = request.POST.get("nombre")
        mascota["especie"] = request.POST.get("especie")
        mascota["raza"] = request.POST.get("raza")
        mascota["nacimiento"] = request.POST.get("nacimiento")
        mascota["propietario"] = request.POST.get("propietario")
        # Aquí podrías guardar la mascota en la base de datos
        return redirect('menu')
    return render(request, "home/menu.html", {"razas_perro": razas_perro, "mascota": {}})

def cerrar_sesion(request):
    logout(request)
    return redirect('index_view')