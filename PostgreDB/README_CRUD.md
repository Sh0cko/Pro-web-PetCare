# PetCare - Sistema de Gestión Veterinaria

Sistema web desarrollado con Django y PostgreSQL para la gestión completa de una clínica veterinaria, con interfaz moderna y sistema de reportes avanzados.

## Características Principales

### 🏥 Gestión Clínica
- **Propietarios**: Gestión de dueños de mascotas
- **Pacientes**: Registro completo de mascotas
- **Citas**: Sistema de calendario para agendar citas (nuevo ✨)
- **Consultas**: Registro de consultas veterinarias
- **Historiales Clínicos**: Historial médico completo de mascotas
- **Vacunas**: Catálogo de vacunas
- **Vacunaciones**: Registro de vacunaciones aplicadas
- **Aseos**: Servicio de baño y aseo
- **Hotel**: Hospedaje para mascotas

### 📦 Catálogo e Inventario
- **Servicios**: Servicios veterinarios disponibles
- **Productos**: Productos en venta con control de stock
- **Inventario**: Control de inventario general
- **Movimientos**: Historial de movimientos de inventario (nuevo ✨)

### 💰 Ventas
- **Tienda**: Catálogo de productos y servicios para venta
- **Carrito**: Sistema de carrito de compras con sesiones
- **Facturas**: Sistema de facturación automatizado
- **Pagos**: Registro de pagos con múltiples métodos

### 📊 Reportes e Inteligencia
- **Stock Bajo**: Alertas de productos con inventario mínimo (nuevo ✨)
- **Caducidad**: Control de productos próximos a caducar o caducados (nuevo ✨)
- **Más Vendidos**: Reporte de productos más vendidos (nuevo ✨)
- **Movimientos**: Historial completo de cambios en inventario (nuevo ✨)

### ⚙️ Administración
- **Empleados**: Personal de la veterinaria
- **Usuarios**: Sistema de autenticación y permisos

## 🎨 Diseño de la Interfaz

El sistema cuenta con un diseño moderno y profesional:

- **Tema Teal**: Paleta de colores consistente con #008b8b como color principal
- **Login Standalone**: Página de inicio de sesión con diseño de tarjeta independiente
- **Sidebar Colapsable**: Navegación organizada en grupos expandibles con iconos de patita 🐾
- **Badges Dinámicos**: Contadores en tiempo real de:
  - Stock bajo (rojo)
  - Productos por caducar (amarillo)
  - Movimientos recientes (azul)
- **Tablas Mejoradas**: Diseño zebra, hover effects, gradientes en encabezados
- **Búsqueda en Todas las Vistas**: Barra de búsqueda en cada CRUD para filtrado rápido
- **Calendario Visual**: Vista de calendario mensual para gestión de citas

## 🆕 Nuevas Características

### Sistema de Inventario Inteligente

El sistema ahora incluye un módulo completo de gestión de inventario:

- **ProductMeta**: Modelo extendido para productos con:
  - Umbral de stock bajo configurable
  - Fecha de caducidad
  - Detección automática de estado de stock
  - Estados de caducidad (OK, Próximo, Caducado)

- **Movimientos de Inventario**: Registro automático de:
  - Entradas (compras, ajustes)
  - Salidas (ventas, mermas)
  - Usuario responsable
  - Timestamp
  - Cantidades anteriores y nuevas

- **Logging Automático**: Se registran movimientos automáticamente al:
  - Crear o actualizar productos
  - Procesar pagos/ventas
  - Realizar ajustes manuales

### Sistema de Reportes

Reportes en tiempo real para toma de decisiones:

1. **Stock Bajo** (`/reportes/stock-bajo/`):
   - Lista de productos bajo el umbral mínimo
   - Stock actual vs. umbral
   - Ordenado por prioridad

2. **Control de Caducidad** (`/reportes/caducidad/`):
   - Productos caducados (en rojo)
   - Productos próximos a caducar (30 días, en amarillo)
   - Ordenado por fecha de caducidad

3. **Más Vendidos** (`/reportes/mas-vendidos/`):
   - Top 10 productos más vendidos
   - Total de cantidad vendida
   - Ordenado por popularidad

4. **Historial de Movimientos** (`/inventario/movimientos/`):
   - Lista completa de cambios en inventario
   - Filtros por tipo (entrada/salida)
   - Búsqueda por producto

### Sistema de Citas

Vista de calendario completa para gestión de citas veterinarias:

- **Calendario Mensual** (`/citas/calendario/`):
  - Vista tipo grid con días del mes
  - Navegación mes anterior/siguiente
  - Mini-tarjetas de citas por día
  - Colores según estado (pendiente, confirmada, completada, cancelada)
  - Click en cita para ver detalles

- **Gestión de Citas**:
  - Crear citas con paciente, servicio, empleado, fecha, hora
  - Estados: PENDIENTE, CONFIRMADA, COMPLETADA, CANCELADA
  - Duración en minutos configurable
  - Motivo y notas adicionales

- **Lista de Citas** (`/citas/`):
  - Vista tabular con búsqueda
  - Filtros por estado
  - Editar/eliminar citas

### Context Processors

El sistema incluye `nav_counters` que calcula en tiempo real:
- Cantidad de productos con stock bajo
- Cantidad de productos próximos a caducar o caducados
- Cantidad de movimientos recientes (últimas 24h)

Estos contadores se muestran como badges en la sidebar.

## Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML5, CSS3 (sin frameworks, diseño custom)
- **Python**: 3.x
- **Template Tags**: Custom filters para calendario
- **Context Processors**: Para badges dinámicos
- **Q Objects**: Búsqueda avanzada en modelos

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

4. **Aplicar migraciones** (IMPORTANTE para nuevas características):
```bash
cd PetCare
python manage.py makemigrations PetApp
python manage.py migrate
```

**Nota**: Las nuevas características (ProductMeta, InventoryMovement, Cita) requieren que ejecutes las migraciones para crear las tablas correspondientes en la base de datos.

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

### URLs Principales
- `/` - Página principal (dashboard)
- `/accounts/login/` - Login (diseño standalone con tarjeta teal)
- `/accounts/logout/` - Cerrar sesión

### Gestión Clínica
- `/propietarios/` - Listado de propietarios
- `/pacientes/` - Listado de pacientes (mascotas)
- `/citas/calendario/` - Vista de calendario de citas 📅 **NUEVO**
- `/citas/` - Lista de citas **NUEVO**
- `/citas/crear/` - Crear nueva cita **NUEVO**
- `/consultas/` - Consultas veterinarias
- `/historiales/` - Historiales clínicos
- `/vacunas/` - Catálogo de vacunas
- `/vacunaciones/` - Registro de vacunaciones
- `/aseos/` - Servicio de aseo
- `/hoteles/` - Hotel para mascotas

### Catálogo e Inventario
- `/servicios/` - Listado de servicios
- `/productos/` - Listado de productos
- `/inventarios/` - Control de inventario
- `/inventario/movimientos/` - Historial de movimientos **NUEVO**

### Ventas
- `/tienda/` - Catálogo de tienda
- `/tienda/carrito/` - Carrito de compras
- `/tienda/checkout/` - Finalizar compra
- `/facturas/` - Facturas
- `/pagos/` - Pagos

### Reportes e Inteligencia
- `/reportes/stock-bajo/` - Alertas de productos con stock bajo 🔴 **NUEVO**
- `/reportes/caducidad/` - Control de productos próximos a caducar 🟡 **NUEVO**
- `/reportes/mas-vendidos/` - Top 10 productos más vendidos 📊 **NUEVO**

### Administración
- `/empleados/` - Listado de empleados
- `/admin/` - Panel de administración de Django

Cada módulo tiene sus propias URLs para crear (`/crear/`), editar (`/editar/<id>/`) y eliminar (`/eliminar/<id>/`) registros.

## Funcionalidades Implementadas

### CRUD Completo con Búsqueda
Cada entidad cuenta con:
- ✅ **Create** (Crear): Formulario para agregar nuevos registros
- ✅ **Read** (Leer): Listado de todos los registros con **barra de búsqueda** 🔍
- ✅ **Update** (Actualizar): Formulario para editar registros existentes
- ✅ **Delete** (Eliminar): Confirmación y eliminación de registros

### Sistema de Inventario Avanzado
- ✅ **Tracking Automático**: Cada cambio en productos se registra automáticamente
- ✅ **Alertas Inteligentes**: Notificaciones de stock bajo y productos próximos a caducar
- ✅ **Reportes Visuales**: Estadísticas y análisis de inventario
- ✅ **Control de Caducidad**: Seguimiento de fechas de vencimiento
- ✅ **Productos Más Vendidos**: Análisis de popularidad

### Sistema de Citas con Calendario
- ✅ **Vista Mensual**: Calendario grid con navegación mes a mes
- ✅ **Estados de Cita**: PENDIENTE, CONFIRMADA, COMPLETADA, CANCELADA
- ✅ **Gestión Completa**: Crear, editar, eliminar citas
- ✅ **Códigos de Color**: Visualización intuitiva según estado
- ✅ **Detalles Completos**: Paciente, servicio, empleado, duración, motivo

### Sistema de Tienda Online
- ✅ **Catálogo de Productos**: Vista de productos disponibles
- ✅ **Carrito de Compras**: Sistema de sesiones para gestión de carrito
- ✅ **Checkout**: Proceso completo de compra con múltiples métodos de pago
- ✅ **Facturación Automática**: Generación de facturas post-venta
- ✅ **Actualización de Stock**: Reducción automática de inventario al procesar ventas

### Características de Interfaz
- ✅ **Mensajes Dinámicos**: Éxito/error para cada operación
- ✅ **Validación de Datos**: Frontend y backend
- ✅ **Relaciones entre Entidades**: ForeignKey y validaciones
- ✅ **Diseño Teal Moderno**: Tema consistente en toda la aplicación
- ✅ **Sidebar Colapsable**: Navegación organizada en grupos
- ✅ **Badges en Tiempo Real**: Contadores de alertas y movimientos
- ✅ **Tablas Mejoradas**: Zebra stripes, hover effects, búsqueda integrada
- ✅ **Responsive**: Adaptado a diferentes tamaños de pantalla

## Notas Importantes

### Modelos de Base de Datos
- **Modelos No Gestionados** (`managed = False`): Los modelos originales (Propietario, Pacientes, Empleado, etc.) no son gestionados por Django. Las tablas deben existir previamente en PostgreSQL.
- **Modelos Nuevos Gestionados** (`managed = True`):
  - `ProductMeta`: Metadata extendida para productos
  - `InventoryMovement`: Registro de movimientos de inventario
  - `Cita`: Sistema de citas veterinarias
  - **Estos modelos requieren que ejecutes las migraciones para crear sus tablas**

### Context Processor
- El sistema incluye un context processor (`nav_counters`) que calcula badges dinámicos
- Está diseñado con fail-safe: si las tablas no existen (pre-migración), devuelve ceros
- Después de ejecutar migraciones, los badges mostrarán datos reales

### Búsqueda
- Todas las vistas CRUD incluyen búsqueda mediante parámetro GET `?q=`
- La búsqueda utiliza Django Q objects para filtros complejos
- Busca en múltiples campos relevantes según el modelo

### Archivos Estáticos
- CSS global en: `PetCare/static/css/style.css`
- No se utilizan frameworks CSS externos (diseño custom)
- Asegúrate de ejecutar `python manage.py collectstatic` en producción

## Solución de Problemas

### Problemas Comunes

**1. Error: "no existe la tabla petapp_productmeta"**
- **Causa**: No se han ejecutado las migraciones para los nuevos modelos
- **Solución**: Ejecuta:
  ```bash
  cd PetCare
  python manage.py makemigrations PetApp
  python manage.py migrate
  ```

**2. Los badges de la sidebar no aparecen o muestran 0**
- **Causa**: Las tablas de ProductMeta/InventoryMovement no existen o están vacías
- **Solución**: Ejecuta las migraciones. El context processor está diseñado para no causar errores, pero necesita las tablas para mostrar datos reales.

**3. Error al buscar en CRUDs**
- **Causa**: Caracteres especiales en el término de búsqueda
- **Solución**: La búsqueda está sanitizada, pero asegúrate de usar términos normales. Si persiste, revisa las Q queries en views.py

**4. El calendario de citas no muestra citas**
- **Causa**: No existen registros en la tabla `Cita` o no se han creado citas
- **Solución**: Crea algunas citas desde `/citas/crear/` y verifica que la migración se ejecutó correctamente

**5. Errores generales de conexión**
- Verifica que el entorno virtual esté activado
- Asegúrate de que PostgreSQL esté corriendo
- Verifica las credenciales de la base de datos en `settings.py`
- Confirma que todas las dependencias estén instaladas (`pip install -r requirements.txt`)

**6. Archivos estáticos no se cargan (CSS no aplica)**
- **Desarrollo**: Asegúrate de tener `DEBUG = True` en settings.py
- **Producción**: Ejecuta `python manage.py collectstatic`
- Verifica que `{% load static %}` esté al inicio de cada template

## Estructura del Proyecto

```
Pro-web-PetCare/
├── PetCare/
│   ├── PetApp/
│   │   ├── models.py              # Modelos (originales + ProductMeta, InventoryMovement, Cita)
│   │   ├── views.py               # Vistas CRUD + reportes + calendario
│   │   ├── admin.py               # Configuración del admin
│   │   ├── context_processors.py # nav_counters para badges dinámicos
│   │   ├── templatetags/
│   │   │   └── calendar_tags.py  # Custom filter get_item para calendario
│   │   └── migrations/            # Migraciones de Django
│   ├── PetCare/
│   │   ├── settings.py            # Configuración (DATABASES, INSTALLED_APPS, context_processors)
│   │   ├── urls.py                # URLs principales
│   │   ├── middleware.py          # Middleware custom (si aplica)
│   │   └── wsgi.py
│   ├── static/
│   │   └── css/
│   │       └── style.css          # Tema teal global (navbar, sidebar, forms, tables, calendar)
│   └── templates/
│       ├── base.html              # Template base con navbar y sidebar colapsable
│       ├── index.html             # Dashboard principal
│       ├── registration/          # Login, logout, password reset
│       │   ├── login.html         # Login standalone con diseño teal
│       │   ├── logged_out.html
│       │   └── password_*.html
│       ├── citas/                 # Sistema de citas (NUEVO)
│       │   ├── calendario.html    # Vista de calendario mensual
│       │   ├── list.html          # Lista de citas
│       │   ├── form.html          # Crear/editar citas
│       │   └── delete.html        # Confirmar eliminación
│       ├── inventario/            # Inventario (NUEVO)
│       │   └── movimientos.html   # Historial de movimientos
│       ├── reportes/              # Reportes (NUEVO)
│       │   ├── low_stock.html     # Productos con stock bajo
│       │   ├── expiration.html    # Control de caducidad
│       │   └── best_sellers.html  # Productos más vendidos
│       ├── tienda/                # Sistema de tienda online
│       │   ├── catalogo.html
│       │   ├── carrito.html
│       │   ├── checkout.html
│       │   └── compra_exitosa.html
│       ├── propietario/           # CRUD Propietarios (list, form, delete)
│       ├── pacientes/             # CRUD Pacientes
│       ├── empleado/              # CRUD Empleados
│       ├── servicio/              # CRUD Servicios
│       ├── producto/              # CRUD Productos
│       ├── inventario/            # CRUD Inventario
│       ├── vacuna/                # CRUD Vacunas
│       ├── vacunacion/            # CRUD Vacunaciones
│       ├── historialclinico/      # CRUD Historiales Clínicos
│       ├── datosconsulta/         # CRUD Consultas
│       ├── aseomascotas/          # CRUD Aseos
│       ├── hotel/                 # CRUD Hotel
│       ├── factura/               # CRUD Facturas
│       └── pago/                  # CRUD Pagos
├── WorkSpace/                     # Entorno virtual Python
│   ├── Scripts/                   # Activación del entorno (activate.bat)
│   └── Lib/site-packages/         # Dependencias instaladas
├── requirements.txt               # Dependencias del proyecto
├── README_CRUD.md                 # Este archivo
└── *.sql                          # Scripts de base de datos
```

## Desarrollado con

- **Django 5.2.7** - Framework web principal
- **PostgreSQL** - Base de datos relacional
- **Python 3.x** - Lenguaje de programación
- **HTML5/CSS3** - Frontend (diseño custom sin frameworks)
- **Python stdlib calendar** - Generación de calendarios mensuales
- **Django Q Objects** - Búsquedas complejas
- **Django Context Processors** - Badges dinámicos
- **Django Template Tags** - Filtros custom

## Próximas Mejoras Sugeridas

- [ ] Dashboard con gráficas de ventas y estadísticas
- [ ] Exportación de reportes a PDF/Excel
- [ ] Sistema de notificaciones push para citas
- [ ] Integración con pasarelas de pago externas
- [ ] App móvil o PWA
- [ ] Sistema de recordatorios por email/SMS
- [ ] Histórico de cambios con auditoría completa
- [ ] Módulo de facturación electrónica
- [ ] Sistema de roles y permisos granulares

## Contribuciones

Para contribuir al proyecto:
1. Crea un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commitea tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

---

**PetCare** - Sistema de Gestión Veterinaria 🐾

*Desarrollado con ❤️ para el cuidado de las mascotas*

