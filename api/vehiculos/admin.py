from django.contrib import admin
from .models import Vehiculos,Estado,Municipio,Localidad

class VehiculosAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Ubicacion_actual_lat','Ubicacion_actual_long','Consumo_combustible','Distancia_recorrida')

class EstadoAdmin(admin.ModelAdmin):
	list_display = ('id','Nombre')	

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ('municipio','Nombre')	

class LocalidadAdmin(admin.ModelAdmin):
	list_display = ('localidad','Nombre','Latitud','Longitud')

admin.site.register(Vehiculos, VehiculosAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
