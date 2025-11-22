from .utils import admin_required, staff_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import (
    Aseomascotas, Datosconsulta, Empleado, Factura, FacturaServicio,
    Historialclinico, Hotel, Inventario, Pacientes, Pago, PagoFactura,
    Producto, Propietario, Servicio, Vacuna, Vacunacion, InventoryMovement, ProductMeta, Cita
)
# ===================== Utilidad para registrar movimientos =====================
def log_movement(producto, change_type, qty_change, previous_qty, new_qty, source=None, note=None, user=None):
    try:
        InventoryMovement.objects.create(
            producto=producto,
            change_type=change_type,
            quantity_change=qty_change,
            previous_quantity=previous_qty,
            new_quantity=new_qty,
            source=source,
            note=note,
            user=user if (user and getattr(user, 'is_authenticated', False)) else None
        )
    except Exception:
        # Evitar que un error de log detenga el flujo principal
        pass

from django.db.models import Q

# Vista principal
@login_required
def index(request):
    return render(request, 'index.html')

# ==================== CRUD PROPIETARIO ====================
def propietario_list(request):
    q = request.GET.get('q', '').strip()
    propietarios = Propietario.objects.all()
    if q:
        propietarios = propietarios.filter(
            Q(nombre__icontains=q) | Q(id_propietario__icontains=q) | Q(email__icontains=q)
        )
    return render(request, 'propietario/list.html', {'propietarios': propietarios, 'q': q})

def propietario_create(request):
    if request.method == 'POST':
        try:
            Propietario.objects.create(
                id_propietario=request.POST['id_propietario'],
                nombre=request.POST['nombre'],
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email'),
                direccion=request.POST.get('direccion')
            )
            messages.success(request, 'Propietario creado exitosamente')
            return redirect('propietario_list')
        except Exception as e:
            messages.error(request, f'Error al crear propietario: {str(e)}')
    return render(request, 'propietario/form.html')

def propietario_update(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        try:
            propietario.nombre = request.POST['nombre']
            propietario.telefono = request.POST.get('telefono')
            propietario.email = request.POST.get('email')
            propietario.direccion = request.POST.get('direccion')
            propietario.save()
            messages.success(request, 'Propietario actualizado exitosamente')
            return redirect('propietario_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar propietario: {str(e)}')
    return render(request, 'propietario/form.html', {'propietario': propietario})

def propietario_delete(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        try:
            propietario.delete()
            messages.success(request, 'Propietario eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar propietario: {str(e)}')
        return redirect('propietario_list')
    return render(request, 'propietario/delete.html', {'propietario': propietario})

# ==================== CRUD PACIENTES ====================
def pacientes_list(request):
    q = request.GET.get('q', '').strip()
    pacientes = Pacientes.objects.select_related('id_propietario').all()
    if q:
        pacientes = pacientes.filter(
            Q(nombre__icontains=q) | Q(especie__icontains=q) | Q(raza__icontains=q) | Q(id_propietario__nombre__icontains=q) | Q(id__icontains=q)
        )
    return render(request, 'pacientes/list.html', {'pacientes': pacientes, 'q': q})

def pacientes_create(request):
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            Pacientes.objects.create(
                id=request.POST['id'],
                nombre=request.POST['nombre'],
                especie=request.POST.get('especie'),
                raza=request.POST.get('raza'),
                nacimiento=request.POST.get('nacimiento') or None,
                id_propietario_id=request.POST.get('id_propietario') or None
            )
            messages.success(request, 'Paciente creado exitosamente')
            return redirect('pacientes_list')
        except Exception as e:
            messages.error(request, f'Error al crear paciente: {str(e)}')
    return render(request, 'pacientes/form.html', {'propietarios': propietarios})

def pacientes_update(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            paciente.nombre = request.POST['nombre']
            paciente.especie = request.POST.get('especie')
            paciente.raza = request.POST.get('raza')
            paciente.nacimiento = request.POST.get('nacimiento') or None
            paciente.id_propietario_id = request.POST.get('id_propietario') or None
            paciente.save()
            messages.success(request, 'Paciente actualizado exitosamente')
            return redirect('pacientes_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar paciente: {str(e)}')
    return render(request, 'pacientes/form.html', {'paciente': paciente, 'propietarios': propietarios})

def pacientes_delete(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    if request.method == 'POST':
        try:
            paciente.delete()
            messages.success(request, 'Paciente eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar paciente: {str(e)}')
        return redirect('pacientes_list')
    return render(request, 'pacientes/delete.html', {'paciente': paciente})

# ==================== CRUD EMPLEADO ====================
def empleado_list(request):
    q = request.GET.get('q', '').strip()
    empleados = Empleado.objects.all()
    if q:
        empleados = empleados.filter(
            Q(nombre__icontains=q) | Q(cargo__icontains=q) | Q(id_empleado__icontains=q)
        )
    return render(request, 'empleado/list.html', {'empleados': empleados, 'q': q})

def empleado_create(request):
    if request.method == 'POST':
        try:
            Empleado.objects.create(
                id_empleado=request.POST['id_empleado'],
                nombre=request.POST['nombre'],
                cargo=request.POST.get('cargo'),
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email')
            )
            messages.success(request, 'Empleado creado exitosamente')
            return redirect('empleado_list')
        except Exception as e:
            messages.error(request, f'Error al crear empleado: {str(e)}')
    return render(request, 'empleado/form.html')

def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        try:
            empleado.nombre = request.POST['nombre']
            empleado.cargo = request.POST.get('cargo')
            empleado.telefono = request.POST.get('telefono')
            empleado.email = request.POST.get('email')
            empleado.save()
            messages.success(request, 'Empleado actualizado exitosamente')
            return redirect('empleado_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar empleado: {str(e)}')
    return render(request, 'empleado/form.html', {'empleado': empleado})

def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        try:
            empleado.delete()
            messages.success(request, 'Empleado eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar empleado: {str(e)}')
        return redirect('empleado_list')
    return render(request, 'empleado/delete.html', {'empleado': empleado})

# ==================== CRUD SERVICIO ====================
def servicio_list(request):
    q = request.GET.get('q', '').strip()
    servicios = Servicio.objects.all()
    if q:
        servicios = servicios.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q) | Q(id_servicio__icontains=q)
        )
    return render(request, 'servicio/list.html', {'servicios': servicios, 'q': q})

def servicio_create(request):
    if request.method == 'POST':
        try:
            Servicio.objects.create(
                id_servicio=request.POST['id_servicio'],
                nombre=request.POST['nombre'],
                descripcion=request.POST.get('descripcion'),
                costo=request.POST.get('costo')
            )
            messages.success(request, 'Servicio creado exitosamente')
            return redirect('servicio_list')
        except Exception as e:
            messages.error(request, f'Error al crear servicio: {str(e)}')
    return render(request, 'servicio/form.html')

def servicio_update(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        try:
            servicio.nombre = request.POST['nombre']
            servicio.descripcion = request.POST.get('descripcion')
            servicio.costo = request.POST.get('costo')
            servicio.save()
            messages.success(request, 'Servicio actualizado exitosamente')
            return redirect('servicio_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar servicio: {str(e)}')
    return render(request, 'servicio/form.html', {'servicio': servicio})

def servicio_delete(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        try:
            servicio.delete()
            messages.success(request, 'Servicio eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar servicio: {str(e)}')
        return redirect('servicio_list')
    return render(request, 'servicio/delete.html', {'servicio': servicio})

# ==================== CRUD PRODUCTO ====================
def producto_list(request):
    q = request.GET.get('q', '').strip()
    productos = Producto.objects.all()
    if q:
        productos = productos.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q) | Q(id_producto__icontains=q)
        )
    return render(request, 'producto/list.html', {'productos': productos, 'q': q})

def producto_create(request):
    if request.method == 'POST':
        try:
            Producto.objects.create(
                id_producto=request.POST['id_producto'],
                nombre=request.POST['nombre'],
                precio=request.POST.get('precio'),
                cantidad=request.POST.get('cantidad'),
                descripcion=request.POST.get('descripcion')
            )
            # Crear meta opcional si viene información
            prod = Producto.objects.get(id_producto=request.POST['id_producto'])
            threshold = request.POST.get('low_stock_threshold')
            expiration = request.POST.get('expiration_date')
            if threshold or expiration:
                ProductMeta.objects.get_or_create(
                    producto=prod,
                    defaults={
                        'low_stock_threshold': int(threshold) if threshold else 5,
                        'expiration_date': expiration if expiration else None
                    }
                )
            log_movement(prod, 'CREACION', int(request.POST.get('cantidad') or 0), 0, int(request.POST.get('cantidad') or 0), source='producto_create', user=request.user)
            messages.success(request, 'Producto creado exitosamente')
            return redirect('producto_list')
        except Exception as e:
            messages.error(request, f'Error al crear producto: {str(e)}')
    return render(request, 'producto/form.html')

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        try:
            prev_qty = producto.cantidad or 0
            producto.nombre = request.POST['nombre']
            producto.precio = request.POST.get('precio')
            producto.cantidad = request.POST.get('cantidad')
            producto.descripcion = request.POST.get('descripcion')
            producto.save()
            # Actualizar meta
            threshold = request.POST.get('low_stock_threshold')
            expiration = request.POST.get('expiration_date')
            if threshold or expiration:
                meta, _ = ProductMeta.objects.get_or_create(producto=producto)
                if threshold:
                    meta.low_stock_threshold = int(threshold)
                if expiration:
                    meta.expiration_date = expiration
                meta.save()
            new_qty = producto.cantidad or 0
            if new_qty != prev_qty:
                log_movement(producto, 'ACTUALIZACION', new_qty - prev_qty, prev_qty, new_qty, source='producto_update', user=request.user)
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('producto_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar producto: {str(e)}')
    return render(request, 'producto/form.html', {'producto': producto})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        try:
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar producto: {str(e)}')
        return redirect('producto_list')
    return render(request, 'producto/delete.html', {'producto': producto})

# ==================== CRUD INVENTARIO ====================
def inventario_list(request):
    q = request.GET.get('q', '').strip()
    inventarios = Inventario.objects.all()
    if q:
        inventarios = inventarios.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q) | Q(id_producto__icontains=q)
        )
    return render(request, 'inventario/list.html', {'inventarios': inventarios, 'q': q})

def inventario_create(request):
    if request.method == 'POST':
        try:
            Inventario.objects.create(
                id_producto=request.POST['id_producto'],
                nombre=request.POST['nombre'],
                descripcion=request.POST.get('descripcion'),
                cantidad=request.POST.get('cantidad'),
                precio=request.POST.get('precio'),
                fecha_actualizacion=request.POST.get('fecha_actualizacion') or None
            )
            messages.success(request, 'Inventario creado exitosamente')
            return redirect('inventario_list')
        except Exception as e:
            messages.error(request, f'Error al crear inventario: {str(e)}')
    return render(request, 'inventario/form.html')

def inventario_update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        try:
            inventario.nombre = request.POST['nombre']
            inventario.descripcion = request.POST.get('descripcion')
            inventario.cantidad = request.POST.get('cantidad')
            inventario.precio = request.POST.get('precio')
            inventario.fecha_actualizacion = request.POST.get('fecha_actualizacion') or None
            inventario.save()
            messages.success(request, 'Inventario actualizado exitosamente')
            return redirect('inventario_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar inventario: {str(e)}')
    return render(request, 'inventario/form.html', {'inventario': inventario})

def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        try:
            inventario.delete()
            messages.success(request, 'Inventario eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar inventario: {str(e)}')
        return redirect('inventario_list')
    return render(request, 'inventario/delete.html', {'inventario': inventario})

# ==================== CRUD VACUNA ====================
def vacuna_list(request):
    q = request.GET.get('q', '').strip()
    vacunas = Vacuna.objects.all()
    if q:
        vacunas = vacunas.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q) | Q(id_vacuna__icontains=q)
        )
    return render(request, 'vacuna/list.html', {'vacunas': vacunas, 'q': q})

def vacuna_create(request):
    if request.method == 'POST':
        try:
            Vacuna.objects.create(
                id_vacuna=request.POST['id_vacuna'],
                nombre=request.POST['nombre'],
                descripcion=request.POST.get('descripcion')
            )
            messages.success(request, 'Vacuna creada exitosamente')
            return redirect('vacuna_list')
        except Exception as e:
            messages.error(request, f'Error al crear vacuna: {str(e)}')
    return render(request, 'vacuna/form.html')

def vacuna_update(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    if request.method == 'POST':
        try:
            vacuna.nombre = request.POST['nombre']
            vacuna.descripcion = request.POST.get('descripcion')
            vacuna.save()
            messages.success(request, 'Vacuna actualizada exitosamente')
            return redirect('vacuna_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar vacuna: {str(e)}')
    return render(request, 'vacuna/form.html', {'vacuna': vacuna})

def vacuna_delete(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    if request.method == 'POST':
        try:
            vacuna.delete()
            messages.success(request, 'Vacuna eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar vacuna: {str(e)}')
        return redirect('vacuna_list')
    return render(request, 'vacuna/delete.html', {'vacuna': vacuna})

# ==================== CRUD VACUNACION ====================
def vacunacion_list(request):
    q = request.GET.get('q', '').strip()
    vacunaciones = Vacunacion.objects.select_related('id_mascota','id_vacuna').all()
    if q:
        vacunaciones = vacunaciones.filter(
            Q(id_vacunacion__icontains=q) | Q(veterinario__icontains=q) | Q(id_mascota__nombre__icontains=q) | Q(id_vacuna__nombre__icontains=q)
        )
    return render(request, 'vacunacion/list.html', {'vacunaciones': vacunaciones, 'q': q})

def vacunacion_create(request):
    pacientes = Pacientes.objects.all()
    vacunas = Vacuna.objects.all()
    if request.method == 'POST':
        try:
            Vacunacion.objects.create(
                id_vacunacion=request.POST['id_vacunacion'],
                id_mascota_id=request.POST.get('id_mascota') or None,
                id_vacuna_id=request.POST.get('id_vacuna') or None,
                fecha=request.POST.get('fecha') or None,
                veterinario=request.POST.get('veterinario')
            )
            messages.success(request, 'Vacunación creada exitosamente')
            return redirect('vacunacion_list')
        except Exception as e:
            messages.error(request, f'Error al crear vacunación: {str(e)}')
    return render(request, 'vacunacion/form.html', {'pacientes': pacientes, 'vacunas': vacunas})

def vacunacion_update(request, pk):
    vacunacion = get_object_or_404(Vacunacion, pk=pk)
    pacientes = Pacientes.objects.all()
    vacunas = Vacuna.objects.all()
    if request.method == 'POST':
        try:
            vacunacion.id_mascota_id = request.POST.get('id_mascota') or None
            vacunacion.id_vacuna_id = request.POST.get('id_vacuna') or None
            vacunacion.fecha = request.POST.get('fecha') or None
            vacunacion.veterinario = request.POST.get('veterinario')
            vacunacion.save()
            messages.success(request, 'Vacunación actualizada exitosamente')
            return redirect('vacunacion_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar vacunación: {str(e)}')
    return render(request, 'vacunacion/form.html', {'vacunacion': vacunacion, 'pacientes': pacientes, 'vacunas': vacunas})

def vacunacion_delete(request, pk):
    vacunacion = get_object_or_404(Vacunacion, pk=pk)
    if request.method == 'POST':
        try:
            vacunacion.delete()
            messages.success(request, 'Vacunación eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar vacunación: {str(e)}')
        return redirect('vacunacion_list')
    return render(request, 'vacunacion/delete.html', {'vacunacion': vacunacion})

# ==================== CRUD HISTORIAL CLINICO ====================
def historialclinico_list(request):
    q = request.GET.get('q', '').strip()
    historiales = Historialclinico.objects.select_related('id_mascota').all()
    if q:
        historiales = historiales.filter(
            Q(id_historial__icontains=q) | Q(id_mascota__nombre__icontains=q) | Q(observaciones__icontains=q)
        )
    return render(request, 'historialclinico/list.html', {'historiales': historiales, 'q': q})

def historialclinico_create(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            Historialclinico.objects.create(
                id_historial=request.POST['id_historial'],
                id_mascota_id=request.POST.get('id_mascota') or None,
                peso=request.POST.get('peso') or None,
                temperatura=request.POST.get('temperatura') or None,
                antecedentes=request.POST.get('antecedentes'),
                tratamientos=request.POST.get('tratamientos'),
                observaciones=request.POST.get('observaciones')
            )
            messages.success(request, 'Historial clínico creado exitosamente')
            return redirect('historialclinico_list')
        except Exception as e:
            messages.error(request, f'Error al crear historial clínico: {str(e)}')
    return render(request, 'historialclinico/form.html', {'pacientes': pacientes})

def historialclinico_update(request, pk):
    historial = get_object_or_404(Historialclinico, pk=pk)
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            historial.id_mascota_id = request.POST.get('id_mascota') or None
            historial.peso = request.POST.get('peso') or None
            historial.temperatura = request.POST.get('temperatura') or None
            historial.antecedentes = request.POST.get('antecedentes')
            historial.tratamientos = request.POST.get('tratamientos')
            historial.observaciones = request.POST.get('observaciones')
            historial.save()
            messages.success(request, 'Historial clínico actualizado exitosamente')
            return redirect('historialclinico_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar historial clínico: {str(e)}')
    return render(request, 'historialclinico/form.html', {'historial': historial, 'pacientes': pacientes})

def historialclinico_delete(request, pk):
    historial = get_object_or_404(Historialclinico, pk=pk)
    if request.method == 'POST':
        try:
            historial.delete()
            messages.success(request, 'Historial clínico eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar historial clínico: {str(e)}')
        return redirect('historialclinico_list')
    return render(request, 'historialclinico/delete.html', {'historial': historial})

# ==================== CRUD DATOS CONSULTA ====================
def datosconsulta_list(request):
    q = request.GET.get('q', '').strip()
    consultas = Datosconsulta.objects.select_related('id_mascota').all()
    if q:
        consultas = consultas.filter(
            Q(id_consulta__icontains=q) | Q(motivo__icontains=q) | Q(id_mascota__nombre__icontains=q) | Q(diagnostico__icontains=q)
        )
    return render(request, 'datosconsulta/list.html', {'consultas': consultas, 'q': q})

def datosconsulta_create(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            Datosconsulta.objects.create(
                id_consulta=request.POST['id_consulta'],
                motivo=request.POST.get('motivo'),
                fecha=request.POST.get('fecha') or None,
                diagnostico=request.POST.get('diagnostico'),
                id_mascota_id=request.POST['id_mascota'],
                detalles_paciente=request.POST.get('detalles_paciente')
            )
            messages.success(request, 'Consulta creada exitosamente')
            return redirect('datosconsulta_list')
        except Exception as e:
            messages.error(request, f'Error al crear consulta: {str(e)}')
    return render(request, 'datosconsulta/form.html', {'pacientes': pacientes})

def datosconsulta_update(request, pk):
    consulta = get_object_or_404(Datosconsulta, pk=pk)
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            consulta.motivo = request.POST.get('motivo')
            consulta.fecha = request.POST.get('fecha') or None
            consulta.diagnostico = request.POST.get('diagnostico')
            consulta.id_mascota_id = request.POST['id_mascota']
            consulta.detalles_paciente = request.POST.get('detalles_paciente')
            consulta.save()
            messages.success(request, 'Consulta actualizada exitosamente')
            return redirect('datosconsulta_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar consulta: {str(e)}')
    return render(request, 'datosconsulta/form.html', {'consulta': consulta, 'pacientes': pacientes})

def datosconsulta_delete(request, pk):
    consulta = get_object_or_404(Datosconsulta, pk=pk)
    if request.method == 'POST':
        try:
            consulta.delete()
            messages.success(request, 'Consulta eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar consulta: {str(e)}')
        return redirect('datosconsulta_list')
    return render(request, 'datosconsulta/delete.html', {'consulta': consulta})

# ==================== CRUD ASEO MASCOTAS ====================
def aseomascotas_list(request):
    q = request.GET.get('q', '').strip()
    aseos = Aseomascotas.objects.select_related('id_mascota','id_propietario').all()
    if q:
        aseos = aseos.filter(
            Q(id_aseo__icontains=q) | Q(id_mascota__nombre__icontains=q) | Q(id_propietario__nombre__icontains=q) | Q(tipo_banio__icontains=q)
        )
    return render(request, 'aseomascotas/list.html', {'aseos': aseos, 'q': q})

def aseomascotas_create(request):
    pacientes = Pacientes.objects.all()
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            Aseomascotas.objects.create(
                id_aseo=request.POST['id_aseo'],
                id_mascota_id=request.POST.get('id_mascota') or None,
                id_propietario_id=request.POST.get('id_propietario') or None,
                tipo_banio=request.POST.get('tipo_banio'),
                es_agresivo=request.POST.get('es_agresivo') == 'on',
                fecha_banio=request.POST.get('fecha_banio') or None
            )
            messages.success(request, 'Aseo creado exitosamente')
            return redirect('aseomascotas_list')
        except Exception as e:
            messages.error(request, f'Error al crear aseo: {str(e)}')
    return render(request, 'aseomascotas/form.html', {'pacientes': pacientes, 'propietarios': propietarios})

def aseomascotas_update(request, pk):
    aseo = get_object_or_404(Aseomascotas, pk=pk)
    pacientes = Pacientes.objects.all()
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            aseo.id_mascota_id = request.POST.get('id_mascota') or None
            aseo.id_propietario_id = request.POST.get('id_propietario') or None
            aseo.tipo_banio = request.POST.get('tipo_banio')
            aseo.es_agresivo = request.POST.get('es_agresivo') == 'on'
            aseo.fecha_banio = request.POST.get('fecha_banio') or None
            aseo.save()
            messages.success(request, 'Aseo actualizado exitosamente')
            return redirect('aseomascotas_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar aseo: {str(e)}')
    return render(request, 'aseomascotas/form.html', {'aseo': aseo, 'pacientes': pacientes, 'propietarios': propietarios})

def aseomascotas_delete(request, pk):
    aseo = get_object_or_404(Aseomascotas, pk=pk)
    if request.method == 'POST':
        try:
            aseo.delete()
            messages.success(request, 'Aseo eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar aseo: {str(e)}')
        return redirect('aseomascotas_list')
    return render(request, 'aseomascotas/delete.html', {'aseo': aseo})

# ==================== CRUD HOTEL ====================
def hotel_list(request):
    q = request.GET.get('q', '').strip()
    hoteles = Hotel.objects.select_related('id_mascota').all()
    if q:
        hoteles = hoteles.filter(
            Q(id_hotel__icontains=q) | Q(habitacion__icontains=q) | Q(id_mascota__nombre__icontains=q)
        )
    return render(request, 'hotel/list.html', {'hoteles': hoteles, 'q': q})

def hotel_create(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            Hotel.objects.create(
                id_hotel=request.POST['id_hotel'],
                id_mascota_id=request.POST.get('id_mascota') or None,
                fecha_ingreso=request.POST['fecha_ingreso'],
                fecha_egreso=request.POST['fecha_egreso'],
                habitacion=request.POST.get('habitacion'),
                observaciones=request.POST.get('observaciones')
            )
            messages.success(request, 'Hotel creado exitosamente')
            return redirect('hotel_list')
        except Exception as e:
            messages.error(request, f'Error al crear hotel: {str(e)}')
    return render(request, 'hotel/form.html', {'pacientes': pacientes})

def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        try:
            hotel.id_mascota_id = request.POST.get('id_mascota') or None
            hotel.fecha_ingreso = request.POST['fecha_ingreso']
            hotel.fecha_egreso = request.POST['fecha_egreso']
            hotel.habitacion = request.POST.get('habitacion')
            hotel.observaciones = request.POST.get('observaciones')
            hotel.save()
            messages.success(request, 'Hotel actualizado exitosamente')
            return redirect('hotel_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar hotel: {str(e)}')
    return render(request, 'hotel/form.html', {'hotel': hotel, 'pacientes': pacientes})

def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        try:
            hotel.delete()
            messages.success(request, 'Hotel eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar hotel: {str(e)}')
        return redirect('hotel_list')
    return render(request, 'hotel/delete.html', {'hotel': hotel})

# ==================== CRUD FACTURA ====================
def factura_list(request):
    q = request.GET.get('q', '').strip()
    facturas = Factura.objects.select_related('id_propietario').all()
    if q:
        facturas = facturas.filter(
            Q(id_factura__icontains=q) | Q(id_propietario__nombre__icontains=q)
        )
    return render(request, 'factura/list.html', {'facturas': facturas, 'q': q})

def factura_create(request):
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            Factura.objects.create(
                id_factura=request.POST['id_factura'],
                id_propietario_id=request.POST.get('id_propietario') or None,
                fecha=request.POST.get('fecha') or None,
                total=request.POST.get('total') or None
            )
            messages.success(request, 'Factura creada exitosamente')
            return redirect('factura_list')
        except Exception as e:
            messages.error(request, f'Error al crear factura: {str(e)}')
    return render(request, 'factura/form.html', {'propietarios': propietarios})

def factura_update(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            factura.id_propietario_id = request.POST.get('id_propietario') or None
            factura.fecha = request.POST.get('fecha') or None
            factura.total = request.POST.get('total') or None
            factura.save()
            messages.success(request, 'Factura actualizada exitosamente')
            return redirect('factura_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar factura: {str(e)}')
    return render(request, 'factura/form.html', {'factura': factura, 'propietarios': propietarios})

def factura_delete(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        try:
            factura.delete()
            messages.success(request, 'Factura eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar factura: {str(e)}')
        return redirect('factura_list')
    return render(request, 'factura/delete.html', {'factura': factura})

# ==================== CRUD PAGO ====================
def pago_list(request):
    q = request.GET.get('q', '').strip()
    pagos = Pago.objects.select_related('id_propietario').all()
    if q:
        pagos = pagos.filter(
            Q(id_pago__icontains=q) | Q(id_propietario__nombre__icontains=q) | Q(metodo__icontains=q)
        )
    return render(request, 'pago/list.html', {'pagos': pagos, 'q': q})

def pago_create(request):
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            Pago.objects.create(
                id_pago=request.POST['id_pago'],
                id_propietario_id=request.POST.get('id_propietario') or None,
                fecha=request.POST.get('fecha') or None,
                monto=request.POST.get('monto') or None,
                metodo=request.POST.get('metodo')
            )
            messages.success(request, 'Pago creado exitosamente')
            return redirect('pago_list')
        except Exception as e:
            messages.error(request, f'Error al crear pago: {str(e)}')
    return render(request, 'pago/form.html', {'propietarios': propietarios})

def pago_update(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    propietarios = Propietario.objects.all()
    if request.method == 'POST':
        try:
            pago.id_propietario_id = request.POST.get('id_propietario') or None
            pago.fecha = request.POST.get('fecha') or None
            pago.monto = request.POST.get('monto') or None
            pago.metodo = request.POST.get('metodo')
            pago.save()
            messages.success(request, 'Pago actualizado exitosamente')
            return redirect('pago_list')
        except Exception as e:
            messages.error(request, f'Error al actualizar pago: {str(e)}')
    return render(request, 'pago/form.html', {'pago': pago, 'propietarios': propietarios})

def pago_delete(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        try:
            pago.delete()
            messages.success(request, 'Pago eliminado exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar pago: {str(e)}')
        return redirect('pago_list')
    return render(request, 'pago/delete.html', {'pago': pago})

# ==================== SISTEMA DE VENTAS/CARRITO ====================
from datetime import date
from decimal import Decimal
import json

def tienda_productos(request):
    """Catálogo de productos y servicios disponibles para la venta"""
    productos = Producto.objects.filter(cantidad__gt=0)  # Solo productos con stock
    servicios = Servicio.objects.all()
    return render(request, 'tienda/catalogo.html', {
        'productos': productos,
        'servicios': servicios
    })

def carrito_ver(request):
    """Ver el carrito de compras"""
    carrito = request.session.get('carrito', {})
    items_carrito = []
    total = Decimal('0.00')
    
    for key, item in carrito.items():
        try:
            # Detectar tipo por clave o marca en el item
            es_servicio = (str(key).startswith('S:') or item.get('tipo') == 'servicio')
            if es_servicio:
                servicio_id = str(key).split(':', 1)[1] if ':' in str(key) else key
                servicio = Servicio.objects.get(id_servicio=servicio_id)
                precio = Decimal(str(item['precio']))
                subtotal = precio * item['cantidad']
                items_carrito.append({
                    'tipo': 'servicio',
                    'obj': servicio,
                    'cantidad': item['cantidad'],
                    'precio': precio,
                    'subtotal': subtotal,
                    'key': key,
                })
                total += subtotal
            else:
                producto_id = key
                producto = Producto.objects.get(id_producto=producto_id)
                precio = Decimal(str(item['precio']))
                subtotal = precio * item['cantidad']
                items_carrito.append({
                    'tipo': 'producto',
                    'obj': producto,
                    'cantidad': item['cantidad'],
                    'precio': precio,
                    'subtotal': subtotal,
                    'key': key,
                })
                total += subtotal
        except (Producto.DoesNotExist, Servicio.DoesNotExist):
            continue
    
    return render(request, 'tienda/carrito.html', {
        'items_carrito': items_carrito,
        'total': total
    })

def carrito_agregar(request, producto_id):
    """Agregar producto al carrito"""
    if request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, id_producto=producto_id)
            cantidad = int(request.POST.get('cantidad', 1))
            
            # Verificar stock disponible
            if cantidad > producto.cantidad:
                messages.error(request, f'Solo hay {producto.cantidad} unidades disponibles')
                return redirect('tienda_productos')
            
            # Obtener o crear carrito en sesión
            carrito = request.session.get('carrito', {})
            
            # Si el producto ya está en el carrito, actualizar cantidad
            if producto_id in carrito:
                nueva_cantidad = carrito[producto_id]['cantidad'] + cantidad
                if nueva_cantidad > producto.cantidad:
                    messages.error(request, f'Solo hay {producto.cantidad} unidades disponibles')
                    return redirect('tienda_productos')
                carrito[producto_id]['cantidad'] = nueva_cantidad
            else:
                carrito[producto_id] = {
                    'nombre': producto.nombre,
                    'precio': float(producto.precio),
                    'cantidad': cantidad
                }
            
            request.session['carrito'] = carrito
            request.session.modified = True
            messages.success(request, f'{producto.nombre} agregado al carrito')
            
        except Exception as e:
            messages.error(request, f'Error al agregar al carrito: {str(e)}')
    
    return redirect('tienda_productos')

def carrito_agregar_servicio(request, servicio_id):
    """Agregar servicio al carrito"""
    if request.method == 'POST':
        try:
            servicio = get_object_or_404(Servicio, id_servicio=servicio_id)
            cantidad = int(request.POST.get('cantidad', 1))

            if cantidad <= 0:
                messages.error(request, 'La cantidad debe ser mayor a 0')
                return redirect('tienda_productos')

            carrito = request.session.get('carrito', {})
            key = f'S:{servicio_id}'

            if key in carrito:
                carrito[key]['cantidad'] += cantidad
            else:
                carrito[key] = {
                    'tipo': 'servicio',
                    'nombre': servicio.nombre,
                    'precio': float(servicio.costo or 0),
                    'cantidad': cantidad,
                }

            request.session['carrito'] = carrito
            request.session.modified = True
            messages.success(request, f'{servicio.nombre} agregado al carrito')
        except Exception as e:
            messages.error(request, f'Error al agregar servicio: {str(e)}')
    return redirect('tienda_productos')

def carrito_actualizar(request, producto_id):
    """Actualizar cantidad en el carrito"""
    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 1))
            producto = get_object_or_404(Producto, id_producto=producto_id)
            
            if cantidad > producto.cantidad:
                messages.error(request, f'Solo hay {producto.cantidad} unidades disponibles')
                return redirect('carrito_ver')
            
            carrito = request.session.get('carrito', {})
            
            if producto_id in carrito:
                if cantidad > 0:
                    carrito[producto_id]['cantidad'] = cantidad
                    messages.success(request, 'Cantidad actualizada')
                else:
                    del carrito[producto_id]
                    messages.success(request, 'Producto eliminado del carrito')
                
                request.session['carrito'] = carrito
                request.session.modified = True
        except Exception as e:
            messages.error(request, f'Error al actualizar carrito: {str(e)}')
    
    return redirect('carrito_ver')

def carrito_actualizar_servicio(request, servicio_id):
    """Actualizar cantidad de un servicio en el carrito"""
    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 1))
            key = f'S:{servicio_id}'
            carrito = request.session.get('carrito', {})
            if key in carrito:
                if cantidad > 0:
                    carrito[key]['cantidad'] = cantidad
                    messages.success(request, 'Cantidad actualizada')
                else:
                    del carrito[key]
                    messages.success(request, 'Servicio eliminado del carrito')
                request.session['carrito'] = carrito
                request.session.modified = True
        except Exception as e:
            messages.error(request, f'Error al actualizar servicio en carrito: {str(e)}')
    return redirect('carrito_ver')

def carrito_eliminar(request, producto_id):
    """Eliminar producto del carrito"""
    try:
        carrito = request.session.get('carrito', {})
        if producto_id in carrito:
            del carrito[producto_id]
            request.session['carrito'] = carrito
            request.session.modified = True
            messages.success(request, 'Producto eliminado del carrito')
    except Exception as e:
        messages.error(request, f'Error al eliminar del carrito: {str(e)}')
    
    return redirect('carrito_ver')

def carrito_eliminar_servicio(request, servicio_id):
    """Eliminar servicio del carrito"""
    try:
        key = f'S:{servicio_id}'
        carrito = request.session.get('carrito', {})
        if key in carrito:
            del carrito[key]
            request.session['carrito'] = carrito
            request.session.modified = True
            messages.success(request, 'Servicio eliminado del carrito')
    except Exception as e:
        messages.error(request, f'Error al eliminar servicio del carrito: {str(e)}')
    return redirect('carrito_ver')

def carrito_vaciar(request):
    """Vaciar todo el carrito"""
    if 'carrito' in request.session:
        del request.session['carrito']
        request.session.modified = True
        messages.success(request, 'Carrito vaciado')
    return redirect('carrito_ver')

@login_required
def checkout(request):
    """Proceso de pago/checkout"""
    carrito = request.session.get('carrito', {})
    
    if not carrito:
        messages.error(request, 'El carrito está vacío')
        return redirect('tienda_productos')
    
    # Calcular items y total
    items_carrito = []
    total = Decimal('0.00')
    
    for key, item in carrito.items():
        try:
            es_servicio = (str(key).startswith('S:') or item.get('tipo') == 'servicio')
            precio = Decimal(str(item['precio']))
            if es_servicio:
                servicio_id = str(key).split(':', 1)[1] if ':' in str(key) else key
                servicio = Servicio.objects.get(id_servicio=servicio_id)
                subtotal = precio * item['cantidad']
                items_carrito.append({
                    'tipo': 'servicio',
                    'obj': servicio,
                    'cantidad': item['cantidad'],
                    'precio': precio,
                    'subtotal': subtotal,
                })
                total += subtotal
            else:
                producto = Producto.objects.get(id_producto=key)
                subtotal = precio * item['cantidad']
                items_carrito.append({
                    'tipo': 'producto',
                    'obj': producto,
                    'cantidad': item['cantidad'],
                    'precio': precio,
                    'subtotal': subtotal,
                })
                total += subtotal
        except (Producto.DoesNotExist, Servicio.DoesNotExist):
            continue
    
    propietarios = Propietario.objects.all()
    
    return render(request, 'tienda/checkout.html', {
        'items_carrito': items_carrito,
        'total': total,
        'propietarios': propietarios
    })

@login_required
def procesar_pago(request):
    """Procesar el pago y crear factura"""
    if request.method == 'POST':
        try:
            carrito = request.session.get('carrito', {})
            
            if not carrito:
                messages.error(request, 'El carrito está vacío')
                return redirect('tienda_productos')
            
            # Obtener datos del formulario
            id_propietario = request.POST.get('id_propietario')
            metodo_pago = request.POST.get('metodo_pago')
            
            if not id_propietario:
                messages.error(request, 'Debe seleccionar un cliente')
                return redirect('checkout')
            
            # Calcular total
            total = Decimal('0.00')
            for key, item in carrito.items():
                subtotal = Decimal(str(item['precio'])) * item['cantidad']
                total += subtotal
            
            # Generar IDs únicos
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            id_factura = f'FAC-{timestamp}'
            id_pago = f'PAG-{timestamp}'
            
            # Crear factura
            factura = Factura.objects.create(
                id_factura=id_factura,
                id_propietario_id=id_propietario,
                fecha=date.today(),
                total=total
            )
            
            # Crear pago
            pago = Pago.objects.create(
                id_pago=id_pago,
                id_propietario_id=id_propietario,
                fecha=date.today(),
                monto=total,
                metodo=metodo_pago
            )
            
            # Actualizar inventario y stock de productos
            for key, item in carrito.items():
                # Solo reducir stock para productos
                if not (str(key).startswith('S:') or item.get('tipo') == 'servicio'):
                    try:
                        producto = Producto.objects.get(id_producto=key)
                        prev_qty = producto.cantidad or 0
                        producto.cantidad -= item['cantidad']
                        producto.save()
                        log_movement(producto, 'VENTA', -item['cantidad'], prev_qty, producto.cantidad or 0, source='checkout', note=f"Factura {id_factura}", user=request.user)
                    except Producto.DoesNotExist:
                        continue
            # Limpiar carrito
            if 'carrito' in request.session:
                del request.session['carrito']
                request.session.modified = True
            messages.success(request, f'¡Compra realizada exitosamente! Factura: {id_factura}')
            return redirect('compra_exitosa', id_factura=id_factura)
        except Exception as e:
            messages.error(request, f'Error al procesar el pago: {str(e)}')
            return redirect('checkout')
    return redirect('checkout')

@login_required
def movimientos_inventario(request):
    q = request.GET.get('q', '').strip()
    movimientos = InventoryMovement.objects.select_related('producto').all()
    if q:
        movimientos = movimientos.filter(producto__nombre__icontains=q) | movimientos.filter(producto__id_producto__icontains=q) | movimientos.filter(change_type__icontains=q)
    return render(request, 'inventario/movimientos.html', {'movimientos': movimientos[:500], 'q': q})

@login_required
def productos_bajo_stock(request):
    productos = Producto.objects.all()
    alertas = []
    for p in productos:
        meta = getattr(p, 'meta', None)
        threshold = meta.low_stock_threshold if meta else 5
        qty = p.cantidad or 0
        if qty <= threshold:
            alertas.append({'producto': p, 'cantidad': qty, 'threshold': threshold})
    return render(request, 'reportes/low_stock.html', {'alertas': alertas})

@login_required
def productos_caducidad(request):
    hoy = timezone.now().date()
    proximos = []
    expirados = []
    metas = ProductMeta.objects.select_related('producto').all()
    for m in metas:
        if m.expiration_date:
            delta = (m.expiration_date - hoy).days
            if delta < 0:
                expirados.append(m)
            elif delta <= 30:
                proximos.append({'meta': m, 'dias': delta})
    return render(request, 'reportes/expiration.html', {'expirados': expirados, 'proximos': proximos})

@login_required
def reporte_mas_vendidos(request):
    # Agregar por movimientos de tipo VENTA (cantidad negativa)
    from django.db.models import Sum
    resumen = (InventoryMovement.objects.filter(change_type='VENTA')
               .values('producto__id_producto', 'producto__nombre')
               .annotate(total_vendido=Sum('quantity_change'))
               .order_by('total_vendido'))  # quantity_change es negativo
    # Convertir a positivo para mostrar
    datos = []
    for r in resumen:
        datos.append({
            'id': r['producto__id_producto'],
            'nombre': r['producto__nombre'],
            'total': abs(r['total_vendido'] or 0)
        })
    return render(request, 'reportes/best_sellers.html', {'productos': datos})


@login_required
def compra_exitosa(request, id_factura):
    """Página de confirmación de compra"""
    try:
        factura = Factura.objects.get(id_factura=id_factura)
        return render(request, 'tienda/compra_exitosa.html', {'factura': factura})
    except Factura.DoesNotExist:
        messages.error(request, 'Factura no encontrada')
        return redirect('tienda_productos')


# ==================== SISTEMA DE CITAS ====================
@login_required
def cita_calendario(request):
    """Vista de calendario mensual para citas."""
    import calendar
    from datetime import datetime, timedelta
    
    # Obtener mes/año de parámetros GET o usar actual
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    # Calcular rango de fechas del mes
    primer_dia = datetime(year, month, 1).date()
    ultimo_dia = (primer_dia.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    
    # Obtener citas del mes
    citas = Cita.objects.filter(fecha__gte=primer_dia, fecha__lte=ultimo_dia).select_related('paciente', 'servicio', 'empleado').order_by('fecha', 'hora')
    
    # Crear estructura de calendario (matriz semanas x días)
    cal = calendar.monthcalendar(year, month)
    
    # Agrupar citas por fecha
    citas_por_dia = {}
    for cita in citas:
        dia_str = str(cita.fecha.day)
        if dia_str not in citas_por_dia:
            citas_por_dia[dia_str] = []
        citas_por_dia[dia_str].append(cita)
    
    # Navegación mes anterior/siguiente
    mes_anterior = primer_dia - timedelta(days=1)
    mes_siguiente = ultimo_dia + timedelta(days=1)
    
    context = {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'calendar_weeks': cal,
        'citas_por_dia': citas_por_dia,
        'mes_anterior': mes_anterior,
        'mes_siguiente': mes_siguiente,
        'hoy': datetime.now().date(),
    }
    return render(request, 'citas/calendario.html', context)


@login_required
def cita_list(request):
    """Lista de todas las citas con búsqueda."""
    q = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '').strip()
    
    citas = Cita.objects.select_related('paciente', 'servicio', 'empleado').all()
    
    if q:
        citas = citas.filter(
            Q(paciente__nombre__icontains=q) |
            Q(motivo__icontains=q) |
            Q(empleado__nombre__icontains=q)
        )
    
    if estado:
        citas = citas.filter(estado=estado)
    
    return render(request, 'citas/list.html', {
        'citas': citas,
        'q': q,
        'estado': estado,
        'estados': Cita.ESTADO_CHOICES,
    })


@login_required
def cita_create(request):
    """Crear nueva cita."""
    pacientes = Pacientes.objects.all()
    servicios = Servicio.objects.all()
    empleados = Empleado.objects.all()
    
    if request.method == 'POST':
        try:
            cita = Cita.objects.create(
                paciente_id=request.POST['paciente'],
                servicio_id=request.POST.get('servicio') or None,
                empleado_id=request.POST.get('empleado') or None,
                fecha=request.POST['fecha'],
                hora=request.POST['hora'],
                duracion_minutos=int(request.POST.get('duracion_minutos', 30)),
                estado=request.POST.get('estado', 'PENDIENTE'),
                motivo=request.POST.get('motivo', ''),
                notas=request.POST.get('notas', ''),
                creado_por=request.user
            )
            messages.success(request, f'Cita creada exitosamente para {cita.fecha} {cita.hora}')
            return redirect('cita_calendario')
        except Exception as e:
            messages.error(request, f'Error al crear cita: {str(e)}')
    
    return render(request, 'citas/form.html', {
        'pacientes': pacientes,
        'servicios': servicios,
        'empleados': empleados,
        'estados': Cita.ESTADO_CHOICES,
    })


@login_required
def cita_update(request, pk):
    """Editar cita existente."""
    cita = get_object_or_404(Cita, pk=pk)
    pacientes = Pacientes.objects.all()
    servicios = Servicio.objects.all()
    empleados = Empleado.objects.all()
    
    if request.method == 'POST':
        try:
            cita.paciente_id = request.POST['paciente']
            cita.servicio_id = request.POST.get('servicio') or None
            cita.empleado_id = request.POST.get('empleado') or None
            cita.fecha = request.POST['fecha']
            cita.hora = request.POST['hora']
            cita.duracion_minutos = int(request.POST.get('duracion_minutos', 30))
            cita.estado = request.POST.get('estado', 'PENDIENTE')
            cita.motivo = request.POST.get('motivo', '')
            cita.notas = request.POST.get('notas', '')
            cita.save()
            messages.success(request, 'Cita actualizada exitosamente')
            return redirect('cita_calendario')
        except Exception as e:
            messages.error(request, f'Error al actualizar cita: {str(e)}')
    
    return render(request, 'citas/form.html', {
        'cita': cita,
        'pacientes': pacientes,
        'servicios': servicios,
        'empleados': empleados,
        'estados': Cita.ESTADO_CHOICES,
    })


@login_required
def cita_delete(request, pk):
    """Eliminar cita."""
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        try:
            cita.delete()
            messages.success(request, 'Cita eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar cita: {str(e)}')
        return redirect('cita_calendario')
    return render(request, 'citas/delete.html', {'cita': cita})

# VISTAS PÚBLICAS - accesibles sin estar logueado
def registrar_usuario(request):
    # Si ya está logueado, redirigir al menú principal
    if request.user.is_authenticated:
        return redirect('menu')
    
    if request.method == 'POST':
        # Aquí irá la lógica para crear usuario
        pass
    
    return render(request, 'registration/registrar_usuario.html')

def registrar_admin(request):
    # Si ya está logueado, redirigir al menú principal
    if request.user.is_authenticated:
        return redirect('menu')
    
    if request.method == 'POST':
        # Aquí irá la lógica para crear admin
        pass
    
    return render(request, 'registration/registrar_admin.html')

def registrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('menu')
    
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            email = request.POST.get('email', '')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            
            # Validaciones
            if password != password_confirm:
                messages.error(request, 'Las contraseñas no coinciden')
                return render(request, 'registration/registrar_usuario.html', {
                    'form_data': request.POST
                })
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este nombre de usuario ya existe')
                return render(request, 'registration/registrar_usuario.html', {
                    'form_data': request.POST
                })
            
            # Crear usuario normal
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_staff=False,
                is_superuser=False
            )
            
            messages.success(request, f'¡Cuenta creada exitosamente! Ahora puedes iniciar sesión como {username}')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Error al crear la cuenta: {str(e)}')
            return render(request, 'registration/registrar_usuario.html', {
                'form_data': request.POST
            })
    
    return render(request, 'registration/registrar_usuario.html')

def registrar_admin(request):
    if request.user.is_authenticated:
        return redirect('menu')
    
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            email = request.POST.get('email')
            codigo_verificacion = request.POST.get('codigo_verificacion', '')
            
            # Validaciones
            if password != password_confirm:
                messages.error(request, 'Las contraseñas no coinciden')
                return render(request, 'registration/registrar_admin.html', {
                    'form_data': request.POST
                })
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este nombre de usuario ya existe')
                return render(request, 'registration/registrar_admin.html', {
                    'form_data': request.POST
                })
            
            # Verificar código de administrador (puedes cambiar este código)
            CODIGO_ADMIN = "ADMIN2024"  # Cámbialo por uno más seguro
            
            if codigo_verificacion == CODIGO_ADMIN:
                # Crear superusuario
                user = User.objects.create_superuser(
                    username=username,
                    password=password,
                    email=email
                )
                messages.success(request, f'¡Cuenta de administrador creada exitosamente! Bienvenido {username}')
            else:
                # Crear usuario staff (puede necesitar activación)
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    is_staff=True,
                    is_superuser=False
                )
                messages.success(request, f'¡Solicitud enviada! Un administrador activará tu cuenta pronto.')
            
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Error al crear la cuenta: {str(e)}')
            return render(request, 'registration/registrar_admin.html', {
                'form_data': request.POST
            })
    
    return render(request, 'registration/registrar_admin.html')





@admin_required
def gestionar_usuarios(request):
    # Solo administradores
    return render(request, 'admin/gestionar_usuarios.html')

@staff_required  
def empleado_list(request):
    # Solo staff y administradores
    return render(request, 'empleado/list.html')

# Vistas normales (accesibles para todos los usuarios autenticados)
from django.contrib.auth.decorators import login_required

@login_required
def pacientes_list(request):
    # Todos los usuarios logueados pueden ver pacientes
    return render(request, 'pacientes/list.html')