from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiculosSerializer,EstadoSerializer,RutaSerializer,ParadasSerializer,LocalidadSerializer,MunicipioSerializer
from .models import Vehiculos,Estado,Municipio,Localidad,Ruta,Paradas
from django.http import HttpResponse

# Create your views here.
class VehiculoView(viewsets.ModelViewSet):
    serializer_class = VehiculosSerializer
    queryset = Vehiculos.objects.all()

class EstadoView(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()

class MunicipioView(viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(Id_estado=self.request.GET.get('Id_estado'))
        return query_set

class LocalidadView(viewsets.ModelViewSet):
    serializer_class = LocalidadSerializer
    queryset = Localidad.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(Id_estado=self.request.GET.get('Id_estado')).filter(Id_municipio=self.request.GET.get('Id_municipio'))
        return query_set

class RutaView(viewsets.ModelViewSet):
    serializer_class = RutaSerializer
    queryset = Ruta.objects.all()

class ParadasView(viewsets.ModelViewSet):
    serializer_class = ParadasSerializer
    queryset = Paradas.objects.all()


def index(request):
    return HttpResponse('Hello, welcome to the index page.')

