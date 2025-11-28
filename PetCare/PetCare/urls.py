"""
URL configuration for PetCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.urls import path, include
from PetApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Autenticación (login, logout, password change/reset)
    path('', include('django.contrib.auth.urls')),
    
    # Reportes e Inventario avanzado
    path('inventario/movimientos/', views.movimientos_inventario, name='movimientos_inventario'),
    path('reportes/stock-bajo/', views.productos_bajo_stock, name='productos_bajo_stock'),
    path('reportes/caducidad/', views.productos_caducidad, name='productos_caducidad'),
    path('reportes/mas-vendidos/', views.reporte_mas_vendidos, name='reporte_mas_vendidos'),
    
    # URLs Propietario
    path('propietarios/', views.propietario_list, name='propietario_list'),
    path('propietarios/crear/', views.propietario_create, name='propietario_create'),
    path('propietarios/editar/<str:pk>/', views.propietario_update, name='propietario_update'),
    path('propietarios/eliminar/<str:pk>/', views.propietario_delete, name='propietario_delete'),
    
    # URLs Pacientes
    path('pacientes/', views.pacientes_list, name='pacientes_list'),
    path('pacientes/crear/', views.pacientes_create, name='pacientes_create'),
    path('pacientes/editar/<str:pk>/', views.pacientes_update, name='pacientes_update'),
    path('pacientes/eliminar/<str:pk>/', views.pacientes_delete, name='pacientes_delete'),
    
    # URLs Empleado
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/crear/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<str:pk>/', views.empleado_update, name='empleado_update'),
    path('empleados/eliminar/<str:pk>/', views.empleado_delete, name='empleado_delete'),
    
    # URLs Servicio
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    path('servicios/editar/<str:pk>/', views.servicio_update, name='servicio_update'),
    path('servicios/eliminar/<str:pk>/', views.servicio_delete, name='servicio_delete'),
    
    # URLs Producto
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/crear/', views.producto_create, name='producto_create'),
    path('productos/editar/<str:pk>/', views.producto_update, name='producto_update'),
    path('productos/eliminar/<str:pk>/', views.producto_delete, name='producto_delete'),
    
    # URLs Inventario
    path('inventarios/', views.inventario_list, name='inventario_list'),
    path('inventarios/crear/', views.inventario_create, name='inventario_create'),
    path('inventarios/editar/<str:pk>/', views.inventario_update, name='inventario_update'),
    path('inventarios/eliminar/<str:pk>/', views.inventario_delete, name='inventario_delete'),
    
    # URLs Vacuna
    path('vacunas/', views.vacuna_list, name='vacuna_list'),
    path('vacunas/crear/', views.vacuna_create, name='vacuna_create'),
    path('vacunas/editar/<str:pk>/', views.vacuna_update, name='vacuna_update'),
    path('vacunas/eliminar/<str:pk>/', views.vacuna_delete, name='vacuna_delete'),
    
    # URLs Vacunacion
    path('vacunaciones/', views.vacunacion_list, name='vacunacion_list'),
    path('vacunaciones/crear/', views.vacunacion_create, name='vacunacion_create'),
    path('vacunaciones/editar/<str:pk>/', views.vacunacion_update, name='vacunacion_update'),
    path('vacunaciones/eliminar/<str:pk>/', views.vacunacion_delete, name='vacunacion_delete'),
    
    # URLs Historial Clinico
    path('historiales/', views.historialclinico_list, name='historialclinico_list'),
    path('historiales/crear/', views.historialclinico_create, name='historialclinico_create'),
    path('historiales/editar/<str:pk>/', views.historialclinico_update, name='historialclinico_update'),
    path('historiales/eliminar/<str:pk>/', views.historialclinico_delete, name='historialclinico_delete'),
    
    # URLs Datos Consulta
    path('consultas/', views.datosconsulta_list, name='datosconsulta_list'),
    path('consultas/crear/', views.datosconsulta_create, name='datosconsulta_create'),
    path('consultas/editar/<str:pk>/', views.datosconsulta_update, name='datosconsulta_update'),
    path('consultas/eliminar/<str:pk>/', views.datosconsulta_delete, name='datosconsulta_delete'),
    
    # URLs Aseo Mascotas
    path('aseos/', views.aseomascotas_list, name='aseomascotas_list'),
    path('aseos/crear/', views.aseomascotas_create, name='aseomascotas_create'),
    path('aseos/editar/<str:pk>/', views.aseomascotas_update, name='aseomascotas_update'),
    path('aseos/eliminar/<str:pk>/', views.aseomascotas_delete, name='aseomascotas_delete'),
    
    # URLs Hotel
    path('hoteles/', views.hotel_list, name='hotel_list'),
    path('hoteles/crear/', views.hotel_create, name='hotel_create'),
    path('hoteles/editar/<str:pk>/', views.hotel_update, name='hotel_update'),
    path('hoteles/eliminar/<str:pk>/', views.hotel_delete, name='hotel_delete'),
    
    # URLs Factura
    path('facturas/', views.factura_list, name='factura_list'),
    path('facturas/crear/', views.factura_create, name='factura_create'),
    path('facturas/editar/<str:pk>/', views.factura_update, name='factura_update'),
    path('facturas/eliminar/<str:pk>/', views.factura_delete, name='factura_delete'),
    
    # URLs Pago
    path('pagos/', views.pago_list, name='pago_list'),
    path('pagos/crear/', views.pago_create, name='pago_create'),
    path('pagos/editar/<str:pk>/', views.pago_update, name='pago_update'),
    path('pagos/eliminar/<str:pk>/', views.pago_delete, name='pago_delete'),
    
    # URLs Sistema de Ventas/Tienda
    path('tienda/', views.tienda_productos, name='tienda_productos'),
    path('carrito/', views.carrito_ver, name='carrito_ver'),
    path('carrito/agregar/<str:producto_id>/', views.carrito_agregar, name='carrito_agregar'),
    path('carrito/agregar-servicio/<str:servicio_id>/', views.carrito_agregar_servicio, name='carrito_agregar_servicio'),
    path('carrito/actualizar/<str:producto_id>/', views.carrito_actualizar, name='carrito_actualizar'),
    path('carrito/actualizar-servicio/<str:servicio_id>/', views.carrito_actualizar_servicio, name='carrito_actualizar_servicio'),
    path('carrito/eliminar/<str:producto_id>/', views.carrito_eliminar, name='carrito_eliminar'),
    path('carrito/eliminar-servicio/<str:servicio_id>/', views.carrito_eliminar_servicio, name='carrito_eliminar_servicio'),
    path('carrito/vaciar/', views.carrito_vaciar, name='carrito_vaciar'),
    path('checkout/', views.checkout, name='checkout'),
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),
    path('compra-exitosa/<str:id_factura>/', views.compra_exitosa, name='compra_exitosa'),
    
    # URLs Citas
    path('citas/calendario/', views.cita_calendario, name='cita_calendario'),
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/editar/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/eliminar/<int:pk>/', views.cita_delete, name='cita_delete'),

    # AUTENTICACIÓN CON TEMPLATES PERSONALIZADOS (una sola vez)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    # URLs DE REGISTRO
    path('accounts/registro/usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('accounts/registro/admin/', views.registrar_admin, name='registrar_admin'),
    
]
