"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from vehiculos import views

router = routers.DefaultRouter()
router.register(r'Vehiculos', views.VehiculoView, 'Vehiculos')
router.register(r'Estado', views.EstadoView, 'Estado')
router.register(r'Municipio', views.MunicipioView, 'Municipio')
router.register(r'Localidad', views.LocalidadView, 'Localidad')
router.register(r'Ruta', views.RutaView, 'Ruta')
router.register(r'Paradas', views.ParadasView, 'Paradas')
router.register(r'RutaVehiculo', views.RutaVehiculosView, 'RutaVehiculo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('', include('vehiculos.urls'))
]

