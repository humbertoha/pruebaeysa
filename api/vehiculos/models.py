from django.db import models
from django.db import connection


# Register your models here.

class Vehiculos(models.Model):
    Ubicacion_actual_lat = models.FloatField()
    Ubicacion_actual_long = models.FloatField()
    Consumo_combustible = models.PositiveIntegerField()
    Distancia_recorrida = models.FloatField()
    Combustible_consumido = models.FloatField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)

class Ruta(models.Model):
    Estatus = models.BooleanField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)

class Paradas(models.Model):
    latitud = models.FloatField()
    Longitud = models.FloatField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)

class Estado(models.Model):
    Nombre = models.CharField(max_length=250)

    @classmethod
    def truncate(cls):
    	with connection.cursor() as cursor:
    		cursor.execute('Truncate Table {} CASCADE'.format(cls._meta.db_table))

class Municipio(models.Model):
    class Meta:
	    constraints = [
	    	models.UniqueConstraint(fields=['id', 'Id_estado'], name='unique_municipio')
	    ]
    municipio = models.IntegerField()
    Nombre = models.CharField(max_length=250)
    Id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    @classmethod
    def truncate(cls):
    	with connection.cursor() as cursor:
    		cursor.execute('Truncate Table {} CASCADE'.format(cls._meta.db_table))

class Localidad(models.Model):
    class Meta:
	    constraints = [
	    	models.UniqueConstraint(fields=['id', 'Id_estado','Id_municipio'], name='unique_localidad')
	    ]
    localidad = models.IntegerField()
    Nombre = models.CharField(max_length=250)
    Latitud = models.FloatField()
    Longitud = models.FloatField()
    Id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    Id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    @classmethod
    def truncate(cls):
    	with connection.cursor() as cursor:
    		cursor.execute('Truncate Table {} CASCADE'.format(cls._meta.db_table))