# Programacion-web-PetCare
Proyecto de programación web

# **Comandos de git (SIEMPRE DESDE EL DIRECTORIO DEL PROYECTO)**

## Requerimientos
```
pip install django pillow requests psycopg2-binary djangorestframework
```
## USUARIO PRO ADMINISTRADOR PRO

user: admin
pass: root

si hay problemas pues bajen que abajo hay instrucciones de como recuperar usuarios o crear nuevos (Inicio de sesion dentro de la app)

##  Descargar repo
Clonar repositorio
```
git clone https://github.com/Sh0cko/Programacion-web-PetCare.git
```
Entrar al directorio del clon del repo
```
cd Programacion-web-PetCare
```
Actualizar tu copia del repo (si alguien lo actualizó)
```
git pull origin main
```
## Subir cambios



### Agregar cambios locales de ficheros a tu copia del repo
```
git add .
```

### Añadir cambios al proyecto en el repositorio
```
git commit -m "Descripción breve de lo que hiciste"
```
```
git push origin main
```
## Comandos para el server

```
python manage.py createsuperuser
```

cambiar password

```
python manage.py createsuperuser
```
# Comandos generales de Django y Python para el proyecto

- ACTIVAR VIRT ENV EN EL PROYECTO

``python
virtualenv -p python3 venv
``

- EJECTUAR VIRT ENV 

``python
source venv/bin/activate
``

- INICIARI PROYECTO CON DJANGO-PYTHON

``python
python -m django startproject demo
``

- CREAR ESTRUCTURA DE HOME DENTRO DEL PROYECTO

``python
python manage.py startapp home
``

- SETTINGS DENTRO DE HOME NECESITAN import os

``python
DIR = DIRECCION DE LA CARPETA TEMPLATES
``
- LA CARPETA TEMPLATES LLEVA DENTRO OTRA CARPETA HOME QUE CONTIENE EL INDEX.HTML

``python
demo/templates/home/index.html
``

- MIGRAR COSAS AL SERVER

``python
python manage.py migrate
``

- CORRER SERVER

``python
python manage.py runserver
``
- USAR EL SHELL PARA LA BD

``python
python manage.py dbshell
``

# Comandos por LaChivaLoca69 sobre la base de datos:

que roio cabezas de huevo ahi les va el tuto de los comandos para el proyecto

# Espacio de trabajo o entorno virtual e instalacion de requisitos etc 
Primero creas el espacio o entorno virtual pue
``` cmd 
# Crear Espacio de trabajo
python -m venv WorkSpace

# Activar (Windows)
WorkSpace\Scripts\activate

# Activar  (Linux/Mac)
source WorkSpace/bin/activate
```
ya activandolo pues instalas el django y psycopg2 (el pscopg2 es para usar postgresql cabesza de huevo no hace falta que te lo diga pedazo de subnormal)
``` cmd
  pip install django
  pip install psycopg2

```
tambien utiliza el sig comando para crear un .txt para cuando compartamos el repo pues nadamas usarlo y no tener que andar poniendo los comandos guarda todas las dependencias, pero igual tienes que saber usar las cosas pendejo de mierda por eso te estoy haciendo el tuto te voy a matar
``` cmd
  pip freeze > requirements.txt
```
Ya instalando todo pues ahora creamos el proyecto y obviamanete te vas a ir a la carpeta del proyecto imbecil 
``` cmd
  django-admin startproject PetCare
  cd PetCare
```
Para el siguiente paso ya tienes que tener instalada la base de datos
# Base de datos 
Te resumo lo que tienes que hacer para crear la base de datos por que deseguro estas bien puñetas cabron 

- Instalas PostgreSql y creas un usuario aparte o con el mismo usuario default sugiero crearlo para asi no cambiar el codigo mas adelante
- Creas la base de datos que ya te pase idiota buscala y le das acceso al usuario nuevo que creas eso es importante 
- y ya we pues es todo ahi van los tutos en chinga congpt alv 

## Pal putito mamador de linux
 1. Instalar PostgreSQL: 
``` cmd
#Actualizar el sistema
sudo pacman -Syu

# Instalar PostgreSQL
sudo pacman -S postgresql

# Para versiones específicas (opcional)
sudo pacman -S postgresql15  # o postgresql14, etc.
```
2. Inicializar el cluster de base de datos:
``` cmd
# Cambiar al usuario postgres
sudo -iu postgres

# Inicializar el cluster (solo primera vez)
initdb --locale=en_US.UTF-8 -D /var/lib/postgres/data

# O usando el método recomendado de Arch:
initdb -D /var/lib/postgres/data
```

3. Habilitar e iniciar el servicio:
``` cmd 
# Salir del usuario postgres
exit

# Habilitar e iniciar PostgreSQL
sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service

# Verificar estado
sudo systemctl status postgresql.service

```
🔧 Configuración y Creación de Usuario/BD
4. Acceder a PostgreSQL:
``` cmd
# Método 1: Cambiar al usuario postgres y acceder
sudo -iu postgres
psql

# Método 2: Directamente
sudo -u postgres psql
```
5. Crear usuario y base de datos:
``` sql
-- Crear usuario con contraseña
CREATE USER mi_usuario WITH PASSWORD 'tu_contraseña_segura';

-- Crear base de datos
CREATE DATABASE mi_base_datos;

-- Asignar propietario
ALTER DATABASE mi_base_datos OWNER TO mi_usuario;

-- Dar todos los privilegios (opcional)
GRANT ALL PRIVILEGES ON DATABASE mi_base_datos TO mi_usuario;

-- Verificar
\du    -- Lista usuarios
\l     -- Lista bases de datos
```
🔐 Configuración de Autenticación
6. Configurar acceso con contraseña:
```
# Editar pg_hba.conf
sudo nano /var/lib/postgres/data/pg_hba.conf
Modificar las líneas para usar md5:

text
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5

# IPv6 local connections:
host    all             all             ::1/128                 md5
```
7. Reiniciar el servicio:
```
sudo systemctl restart postgresql.service
```
🚀 Conectarse a la Base de Datos
8. Probar la conexión:
```
# Conectar con el nuevo usuario
psql -h localhost -U mi_usuario -d mi_base_datos
```
# O desde el usuario postgres asignando propiedad
``` sudo -u postgres psql -d mi_base_datos ``` 
## Pa los cabros que deseguro ni lo van a hacer 
- Pon atencion cabron lo que tienes que hacer es abrir el pgadmin4 y creas la base de datos 
<img width="441" height="152" alt="image" src="https://gist.github.com/user-attachments/assets/b79b6de7-055b-4f7a-b644-03c3d404c205" />

- Luego la creas pones el nombre y te vas a seguridad y agregas los usuarios PERO LOS PONES WEEEE

<img width="692" height="448" alt="image" src="https://gist.github.com/user-attachments/assets/253005f6-800c-4da5-a77b-99a1563f1452" />

- Dale todos los privilegios y pues la creas. 
- Ahora tienes que hacer lo siguiente irte a querytool obviamente en la base de datos
<img width="360" height="526" alt="image" src="https://gist.github.com/user-attachments/assets/7a01cf02-161b-43f0-96d3-03e6a7b5780c" />

- Pegas el script de la base de datos obviamente sin el create database putisimo subnormal animal y le das F5 PERO LE DAS F5 APRENDE A LEER COMO SE TE OCURRA PREGUNTARME TE DEGOLLLO PUTISIMO ESTUPIDO O PREGUNTALE A CHATGPT IMBECIL
# creacion de la app 
Seguimos con el tuto cawn, antes de eso haz lo siguiente en vamos a la terminal y pon el sig comando
``` cmd
# Crear aplicación
python manage.py PetApp
```

# Conectar la base de datos en el proyecto 

ahora iremos a la carpeta del proyecto vas a ver que si lo hiciste como yo serian 2 Petcare y dentro de ella otra mas llamda igual junto con un archivo manage.py pues ahi vas a crear otro folder llamado templates asi pendejo wuacha. 
-
<img width="194" height="265" alt="image" src="https://gist.github.com/user-attachments/assets/af5869a6-2b28-42f7-8180-edadf6aa4cbb" />

Ahora te dejas de mamadas y te vas a la carpeta PetCare al archivo settings.py y en 'DIRS' Agregas "templates" 
``` python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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
dentro de settings tambien cambias el apartado DATABASE por el siguiente
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PetCareDB',
        'USER': 'Admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',  # o la IP de tu servidor
        'PORT': '5432',  
        'OPTIONS': {
            'client_encoding': 'UTF8',
            },
    }
}
```
lo que estas haciendo es conectar tu usuario por el nuevo aparte especificando que estas usando postgresql.
Obvio que si tu usuario no es admin y tu contra no es admin123 no va a jalar pedazo de subnormal neta te crees ingeniero? 8vo semestre puro pinche profe barco vales verga sopla pollas.

bueno con esto ya hecho pues nos vamos a la terminal y hacemos lo siguiente dentro de la primera carpeta petcare y obviamente dentro del entorno pendjeo idiota.

``` cmd
# Genera los modelos 
python manage.py inspectdb > models.py

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

``` 
ah y pon models.py en petapp por que de ahi la vamos a estar usando.
Con este tuto pues ya te sabes los comandos para crear y andarle moviendo al pinche proyecto ponte a chambear hijo de la chingada.
<img width="1200" height="2995" alt="image" src="https://gist.github.com/user-attachments/assets/404228c4-34d3-4480-bc44-b18fe743cba7" />
