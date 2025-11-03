# PetCare - Sistema de Gestión Veterinaria

Sistema web desarrollado con Django y PostgreSQL para la gestión completa de una clínica veterinaria.

## Características

El sistema incluye CRUD completo para las siguientes entidades:

- **Propietarios**: Gestión de dueños de mascotas
- **Pacientes**: Registro de mascotas
- **Empleados**: Personal de la veterinaria
- **Servicios**: Servicios veterinarios disponibles
- **Productos**: Productos en venta
- **Inventario**: Control de inventario
- **Vacunas**: Catálogo de vacunas
- **Vacunaciones**: Registro de vacunaciones aplicadas
- **Historiales Clínicos**: Historial médico de mascotas
- **Consultas**: Registro de consultas veterinarias
- **Aseos**: Servicio de baño y aseo
- **Hotel**: Hospedaje para mascotas
- **Facturas**: Sistema de facturación
- **Pagos**: Registro de pagos

## Requisitos Previos

- Python 3.x
- PostgreSQL
- pip (gestor de paquetes de Python)

## Instalación

1. **Activar el entorno virtual** (ya existe en el proyecto):
```bash
cd "d:\Archivos\Trabajos VC\ProWeb"
WorkSpace\Scripts\activate
```

2. **Instalar dependencias** (si es necesario):
```bash
pip install -r requirements.txt
```

3. **Configurar la base de datos**:
   - Asegúrate de que PostgreSQL esté ejecutándose
   - La base de datos ya está configurada en `settings.py`

4. **Aplicar migraciones** (si es necesario):
```bash
cd PetCare
python manage.py migrate
```

## Ejecución

1. **Activar el entorno virtual** (si no está activado):
```bash
WorkSpace\Scripts\activate
```

2. **Iniciar el servidor**:
```bash
cd PetCare
python manage.py runserver
```

3. **Acceder al sistema**:
   - Abre tu navegador y ve a: `http://127.0.0.1:8000/`
   - Para el panel de administración: `http://127.0.0.1:8000/admin/`

## Estructura de URLs

- `/` - Página principal
- `/propietarios/` - Listado de propietarios
- `/pacientes/` - Listado de pacientes (mascotas)
- `/empleados/` - Listado de empleados
- `/servicios/` - Listado de servicios
- `/productos/` - Listado de productos
- `/inventarios/` - Control de inventario
- `/vacunas/` - Catálogo de vacunas
- `/vacunaciones/` - Registro de vacunaciones
- `/historiales/` - Historiales clínicos
- `/consultas/` - Consultas veterinarias
- `/aseos/` - Servicio de aseo
- `/hoteles/` - Hotel para mascotas
- `/facturas/` - Facturas
- `/pagos/` - Pagos

Cada módulo tiene sus propias URLs para crear, editar y eliminar registros.

## Funcionalidades Implementadas

### CRUD Completo
Cada entidad cuenta con:
- ✅ **Create** (Crear): Formulario para agregar nuevos registros
- ✅ **Read** (Leer): Listado de todos los registros
- ✅ **Update** (Actualizar): Formulario para editar registros existentes
- ✅ **Delete** (Eliminar): Confirmación y eliminación de registros

### Características Adicionales
- Mensajes de éxito/error para cada operación
- Validación de datos
- Relaciones entre entidades (ForeignKey)
- Interfaz intuitiva con navegación fácil
- Diseño responsive

## Notas

- El sistema está configurado para trabajar con la base de datos PostgreSQL existente
- Los modelos están marcados como `managed = False`, lo que significa que Django no creará ni modificará las tablas
- Las tablas deben existir previamente en la base de datos
- El diseño de la interfaz es funcional y simple, enfocado en la funcionalidad CRUD

## Solución de Problemas

Si encuentras errores al ejecutar:

1. Verifica que el entorno virtual esté activado
2. Asegúrate de que PostgreSQL esté corriendo
3. Verifica las credenciales de la base de datos en `settings.py`
4. Confirma que todas las dependencias estén instaladas

## Estructura del Proyecto

```
PetCare/
├── PetApp/
│   ├── models.py          # Modelos de la base de datos
│   ├── views.py           # Lógica de las vistas CRUD
│   └── admin.py           # Configuración del admin
├── PetCare/
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py            # URLs principales
│   └── wsgi.py
└── templates/
    ├── base.html          # Plantilla base
    ├── index.html         # Página principal
    ├── propietario/       # Templates de propietarios
    ├── pacientes/         # Templates de pacientes
    ├── empleado/          # Templates de empleados
    ├── servicio/          # Templates de servicios
    ├── producto/          # Templates de productos
    ├── inventario/        # Templates de inventario
    ├── vacuna/            # Templates de vacunas
    ├── vacunacion/        # Templates de vacunaciones
    ├── historialclinico/  # Templates de historiales
    ├── datosconsulta/     # Templates de consultas
    ├── aseomascotas/      # Templates de aseos
    ├── hotel/             # Templates de hotel
    ├── factura/           # Templates de facturas
    └── pago/              # Templates de pagos
```

## Desarrollado con

- Django 5.2.7
- PostgreSQL
- Python 3.x
- HTML/CSS

---

**PetCare** - Sistema de Gestión Veterinaria 🐾
