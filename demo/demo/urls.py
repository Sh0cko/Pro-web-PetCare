"""
URL configuration for demo project.

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
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index_view"),
    path('registro_de_paciente/', views.menu, name="menu"),
    path('buscar_pacientes/', views.buscar_pacientes, name="buscar_pacientes"),
    path('logout/', views.cerrar_sesion, name="logout"),
    path('hospedaje/', views.hospedaje, name="hospedaje"),

    path('registrar_consulta/', views.registrar_consulta, name='registrar_consulta'),
    path('buscar_consulta/', views.buscar_consultas, name='buscar_consultas'),
]