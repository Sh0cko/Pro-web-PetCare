# PetCare - Sistema Web de Gestión Veterinaria

Proyecto web desarrollado con Django y PostgreSQL para la gestión de servicios veterinarios.

---

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación Rápida](#instalación-rápida)
- [Configuración del Entorno](#configuración-del-entorno)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Comandos Django](#comandos-django)
- [Control de Versiones (Git)](#control-de-versiones-git)
- [Credenciales de Acceso](#credenciales-de-acceso)

---

##  Requisitos Previos

- Python 3.8+
- PostgreSQL 12+
- Git

---

## Credenciales

### Usuario Administrador de la Aplicación

- **Usuario**: `petcareadmin`
- **Contraseña**: `root`

### Rol dentro de PostgreSQL
- **DB-Name**: `petcare_database`,
- **Usuario**: `petcare-administrator`,          
- **Contraseña**: `root123`, 


##  Instalación Rápida

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Sh0cko/Programacion-web-PetCare.git
cd Programacion-web-PetCare
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install django pillow requests psycopg2-binary djangorestframework
```

---

##  Configuración del Entorno

### Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate

# Activar entorno virtual (Windows)
venv\Scripts\activate
```

### Guardar Dependencias

```bash
pip freeze > requirements.txt
```

---

##  Configuración de la Base de Datos

### PostgreSQL en Linux (Arch/Manjaro)

#### 1. Instalar PostgreSQL

```bash
# Actualizar el sistema
sudo pacman -Syu

# Instalar PostgreSQL
sudo pacman -S postgresql
```

#### 2. Inicializar PostgreSQL

```bash
# Cambiar al usuario postgres
sudo -iu postgres

# Inicializar el cluster (primera vez)
initdb --locale=en_US.UTF-8 -D /var/lib/postgres/data

# Salir del usuario postgres
exit
```

#### 3. Habilitar e Iniciar Servicio

```bash
# Habilitar e iniciar PostgreSQL
sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service

# Verificar estado
sudo systemctl status postgresql.service
```

#### 4. Crear Usuario y Base de Datos

```bash
# Acceder a PostgreSQL
sudo -u postgres psql
```

```sql
-- Crear usuario
CREATE USER petcare_admin WITH PASSWORD 'tu_contraseña_segura';

-- Crear base de datos
CREATE DATABASE PetCareDB;

-- Asignar propietario
ALTER DATABASE PetCareDB OWNER TO petcare_admin;

-- Otorgar todos los privilegios
GRANT ALL PRIVILEGES ON DATABASE PetCareDB TO petcare_admin;

-- Verificar usuarios y bases de datos
\du
\l

-- Salir
\q
```

#### 5. Configurar Autenticación

```bash
# Editar archivo de configuración
sudo nano /var/lib/postgres/data/pg_hba.conf
```

Modificar las líneas para usar autenticación `md5`:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5

# IPv6 local connections:
host    all             all             ::1/128                 md5
```

```bash
# Reiniciar servicio
sudo systemctl restart postgresql.service
```

#### 6. Probar Conexión

```bash
psql -h localhost -U petcare_admin -d PetCareDB
```

### PostgreSQL en Windows (usando pgAdmin4)

1. **Abrir pgAdmin4** y crear una nueva base de datos
2. **Configurar el nombre**: `PetCareDB`
3. **Ir a Security** y agregar el usuario con todos los privilegios
4. **Abrir Query Tool** en la base de datos creada
5. **Ejecutar el script** de estructura (ubicado en `/PostgreDB/Estructura.sql`)
   - **Importante**: No incluir la línea `CREATE DATABASE` si ya existe

---

## ⚙️ Configuración de Django

### 1. Configurar settings.py

En `demo/demo/settings.py`, modificar:

#### Templates

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],  # Agregar esta línea
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### Base de Datos

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PetCareDB',
        'USER': 'petcare_admin',  # Tu usuario de PostgreSQL
        'PASSWORD': 'tu_contraseña',  # Tu contraseña
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
    }
}
```

### 2. Migraciones

```bash
# Navegar a la carpeta del proyecto
cd demo

# Generar modelos desde la base de datos existente (si aplica)
python manage.py inspectdb > home/models.py

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 3. Crear Superusuario para poder iniciar sesion en la app

```bash
python manage.py createsuperuser
```

### 4. Ejecutar Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

---

##  Comandos Django Útiles

```bash
# Crear nuevo proyecto
django-admin startproject nombre_proyecto

# Crear nueva aplicación
python manage.py startapp nombre_app

# Ejecutar shell de Django
python manage.py shell

# Ejecutar shell de base de datos
python manage.py dbshell

# Crear migraciones
python manage.py makemigrations


# Aplicar migraciones IMPORTANTE
python manage.py migrate

# Correr servidor de desarrollo IMPORTANTE
python manage.py runserver

```

---

##  Control de Versiones (Git)

### Comandos Básicos

```bash
# Ver estado de cambios
git status

# Actualizar tu copia local
git pull origin main

# Agregar todos los cambios locales
git add .

# Hacer commit de cambios
git commit -m "Descripción clara de los cambios"

# Subir cambios al repositorio
git push origin main
```

### Buenas Prácticas

- Siempre ejecutar `git pull` antes de empezar a trabajar
- Hacer commits frecuentes con mensajes descriptivos
- Revisar cambios con `git status` antes de hacer commit
- No subir archivos de configuración sensibles (contraseñas, etc.)

---

## 🔐 Credenciales de Acceso

### Usuario Administrador de la Aplicación

- **Usuario**: `petcareadmin`
- **Contraseña**: `root`

**Nota**: Si tienes problemas para iniciar sesión, puedes crear un nuevo superusuario con:

```bash
python manage.py createsuperuser
```

O cambiar la contraseña de un usuario existente:

```bash
python manage.py changepassword admin
```

---

##  Estructura del Proyecto

```
Pro-web-PetCare/
├── demo/                   # Proyecto Django principal
│   ├── demo/              # Configuración del proyecto
│   │   ├── settings.py    # Configuraciones
│   │   ├── urls.py        # URLs principales
│   │   └── wsgi.py        # Configuración WSGI
│   ├── home/              # Aplicación principal
│   │   ├── models.py      # Modelos de datos
│   │   ├── views.py       # Vistas
│   │   └── admin.py       # Configuración admin
│   ├── templates/         # Plantillas HTML
│   ├── static/            # Archivos estáticos (CSS, JS, img)
│   └── manage.py          # Script de gestión Django
├── PostgreDB/             # Scripts de base de datos
│   ├── Estructura.sql     # Estructura de la BD en SQL
│   └── readme,md          # Informacion sobre la BD
└── requirements.txt       # Dependencias del proyecto
```

---

##  Solución de Problemas

### Error de Conexión a PostgreSQL

- Verificar que el servicio esté corriendo: `sudo systemctl status postgresql`
- Verificar credenciales en `settings.py`
- Revisar archivo `pg_hba.conf` para permisos de autenticación


### Puerto 8000 en Uso

```bash
# Usar otro puerto
python manage.py runserver 8080
```

---

## 👥 Equipo de Desarrollo

Proyecto desarrollado por el equipo de Programación Web

---

## 📄 Licencia

Este proyecto es de uso académico.
