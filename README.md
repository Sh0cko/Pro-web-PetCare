# Programacion-web-PetCare
Proyecto de programación web

## **Comandos de git (SIEMPRE DESDE EL DIRECTORIO DEL PROYECTO)**
## Descargar repo
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

### Sincronizar datos locales a los del repositorio
```
git pull origin main
```

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

# Comandos generales de Django y Python para el proyecto

ACTIVAR VIRT ENV EN EL PROYECTO
``python
virtualenv -p python3 venv
``

EJECTUAR VIRT ENV 
``python
source venv/bin/activate
``

INICIARI PROYECTO CON DJANGO-PYTHON
``python
python -m django startproject demo
``

CREAR ESTRUCTURA DE HOME DENTRO DEL PROYECTO
``python
python manage.py startapp home
``

SETTINGS DENTRO DE HOME NECESITAN import os
``python
DIR = DIRECCION DE LA CARPETA TEMPLATES
``
LA CARPETA TEMPLATES LLEVA DENTRO OTRA CARPETA HOME QUE CONTIENE EL INDEX.HTML
demo/templates/home/index.html

MIGRAR COSAS AL SERVER
python manage.py migrate

CORRER SERVER
python manage.py runserver

USAR EL SHELL PARA LA BD
python manage.py dbshell
