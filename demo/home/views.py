from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Propietario, Paciente, Hotel

@login_required(login_url='/')
def hospedaje(request):
    # Obtener parámetro de búsqueda
    busqueda = request.GET.get('buscar', '').strip()
    
    # Obtener todos los registros de hospedaje o filtrar por búsqueda
    if busqueda:
        hospedajes = Hotel.objects.select_related('id_mascota').filter(
            id_hotel__icontains=busqueda
        ) | Hotel.objects.select_related('id_mascota').filter(
            id_mascota__nombre__icontains=busqueda
        ) | Hotel.objects.select_related('id_mascota').filter(
            id_mascota__id__icontains=busqueda
        )
        hospedajes = hospedajes.order_by('-fecha_ingreso')
    else:
        hospedajes = Hotel.objects.select_related('id_mascota').all().order_by('-fecha_ingreso')
    
    if request.method == 'POST':
        # Verificar si es una acción de eliminar
        accion = request.POST.get('accion')
        
        if accion == 'eliminar':
            id_hotel = request.POST.get('id_hotel_eliminar')
            try:
                hospedaje = Hotel.objects.get(id_hotel=id_hotel)
                nombre_mascota = hospedaje.id_mascota.nombre
                hospedaje.delete()
                messages.success(request, f"Hospedaje {id_hotel} de {nombre_mascota} eliminado exitosamente")
                return redirect('hospedaje')
            except Hotel.DoesNotExist:
                messages.error(request, f"El hospedaje con ID {id_hotel} no existe")
                return redirect('hospedaje')
            except Exception as e:
                messages.error(request, f"Error al eliminar: {str(e)}")
                return redirect('hospedaje')
        
        # Si no es eliminar, es crear
        try:
            # Obtener datos del formulario
            id_hotel = request.POST.get('id_hotel')
            id_mascota = request.POST.get('id_mascota')
            fecha_ingreso = request.POST.get('fecha_ingreso')
            fecha_egreso = request.POST.get('fecha_egreso')
            habitacion = request.POST.get('habitacion', '')
            observaciones = request.POST.get('observaciones', '')
            
            # Validaciones
            if not all([id_hotel, id_mascota, fecha_ingreso, fecha_egreso]):
                messages.error(request, "Por favor complete todos los campos obligatorios")
                return redirect('hospedaje')
            
            # Verificar que la mascota existe
            try:
                mascota = Paciente.objects.get(id=id_mascota)
            except Paciente.DoesNotExist:
                messages.error(request, f"La mascota con ID {id_mascota} no existe")
                return redirect('hospedaje')
            
            # Verificar que el ID de hospedaje no exista
            if Hotel.objects.filter(id_hotel=id_hotel).exists():
                messages.warning(request, f"Ya existe un hospedaje con ID {id_hotel}")
                return redirect('hospedaje')
            
            # Crear el registro de hospedaje
            hospedaje = Hotel.objects.create(
                id_hotel=id_hotel,
                id_mascota=mascota,
                fecha_ingreso=fecha_ingreso,
                fecha_egreso=fecha_egreso,
                habitacion=habitacion,
                observaciones=observaciones
            )
            
            messages.success(request, f"Hospedaje {id_hotel} registrado exitosamente para {mascota.nombre}")
            return redirect('hospedaje')
            
        except Exception as e:
            messages.error(request, f"Error al registrar hospedaje: {str(e)}")
            return redirect('hospedaje')
    
    context = {
        'hospedajes': hospedajes,
        'busqueda': busqueda
    }
    
    return render(request, "home/hospedaje.html", context)


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
        "Siamés", "Persa", "Maine Coon", "Bengala", "Sphynx", "Ragdoll", 
        "British Shorthair", "Abisinio", "Escocés", "Noruego", "Sin especificar"
    ]

    razas_perro = [
        "Chihuahua", "Pug", "Pastor Alemán", "Labrador", "Golden Retriever", 
        "Bulldog", "Beagle", "Dálmata", "Boxer", "Shih Tzu", "Pomerania", 
        "Pitbull", "Schnauzer", "Doberman", "Rottweiler", "Cocker Spaniel", 
        "Border Collie", "Husky", "Samoyedo", "Akita", "Sin especificar"
    ]

    # Obtener todas las mascotas para mostrar en la tabla
    mascotas = Paciente.objects.select_related('id_propietario').all()

    if request.method == "POST":
        try:
            # Obtener datos del formulario
            id_propietario = request.POST.get("id_propietario")
            nombre_propietario = request.POST.get("nombre_propietario")
            telefono_propietario = request.POST.get("telefono_propietario")
            email_propietario = request.POST.get("email_propietario")
            direccion_propietario = request.POST.get("direccion_propietario")
            
            id_mascota = request.POST.get("id_mascota")
            nombre_mascota = request.POST.get("nombre")
            especie = request.POST.get("especie")
            raza = request.POST.get("raza")
            nacimiento = request.POST.get("nacimiento")
            sexo = request.POST.get("sexo")
            color = request.POST.get("color")

            # Validaciones básicas
            if not all([id_propietario, nombre_propietario, id_mascota, nombre_mascota, especie, raza, nacimiento, sexo]):
                messages.error(request, "Por favor complete todos los campos obligatorios (*)")
                return redirect('menu')

            # Crear o actualizar propietario
            propietario, created = Propietario.objects.get_or_create(
                id_propietario=id_propietario,
                defaults={
                    'nombre': nombre_propietario,
                    'telefono': telefono_propietario or '',
                    'email': email_propietario or '',
                    'direccion': direccion_propietario or ''
                }
            )

            # Si el propietario ya existe, actualizar sus datos
            if not created:
                propietario.nombre = nombre_propietario
                propietario.telefono = telefono_propietario or propietario.telefono
                propietario.email = email_propietario or propietario.email
                propietario.direccion = direccion_propietario or propietario.direccion
                propietario.save()

            # Verificar si la mascota ya existe
            if Paciente.objects.filter(id=id_mascota).exists():
                messages.warning(request, f"La mascota con ID {id_mascota} ya existe")
                return redirect('menu')

            # Crear la mascota
            mascota = Paciente.objects.create(
                id=id_mascota,
                nombre=nombre_mascota,
                especie=especie,
                raza=raza,
                nacimiento=nacimiento,
                sexo=sexo,
                color=color or '',
                id_propietario=propietario
            )

            messages.success(request, f"Mascota {nombre_mascota} registrada exitosamente!")
            return redirect('menu')

        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return redirect('menu')

    # Contexto para el template
    context = {
        "razas_perro": razas_perro,
        "razas_gatos": razas_gatos,
        "mascotas": mascotas,
        "mascota": {}  # Para compatibilidad con el formulario
    }
    
    return render(request, "home/menu.html", context)

def cerrar_sesion(request):
    logout(request)
    return redirect('index_view')