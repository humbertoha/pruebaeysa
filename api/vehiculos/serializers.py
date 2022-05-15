from rest_framework import serializers
from .models import Vehiculos,Estado,Municipio,Localidad,Ruta,Paradas,Ruta_Vehiculos



class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id','Nombre']

class MunicipioSerializer(serializers.ModelSerializer):
    Id_estado = EstadoSerializer(read_only=True)

    class Meta:
        model = Municipio
        fields = ['id','Nombre','Id_estado']

class LocalidadSerializer(serializers.ModelSerializer):
    Id_municipio = MunicipioSerializer(read_only=True)
    Id_estado = EstadoSerializer(read_only=True)
    class Meta:
        model = Municipio
        fields = ['id','Nombre','Id_municipio','Id_estado']

class ParadasSerializer(serializers.ModelSerializer):  
    Id_localidad = LocalidadSerializer(read_only=True)
    class Meta:
        model = Paradas
        fields = ['id','id_ruta','Id_localidad']

class RutaSerializer(serializers.ModelSerializer):
    paradas =  serializers.SerializerMethodField('get_Paradas')
    class Meta:
        model = Ruta
        fields = ['id','Nombre','Estatus','paradas']    
    def get_Paradas(self,obj):
        paradas = obj
        queryset = Paradas.objects.filter(id_ruta=paradas).all()
        serializer = ParadasSerializer(queryset,many=True)
        return serializer.data

    def create(self, validated_data):
        paradadata = self.context['request'].data.get('paradas','[]')
        ruta_new = Ruta.objects.create(**validated_data)
        for data in paradadata:
            id_ = int(data.get('Id_localidad').get('id')) 
            localidad_objeto = Localidad.objects.get(id=id_)
            del data['Id_localidad']
            parada = Paradas.objects.create(id_ruta=ruta_new,Id_localidad=localidad_objeto)
        return ruta_new 

    def update(self, instance, validated_data):
        instance.Nombre = validated_data.get("Nombre",instance.Nombre)
        instance.Estatus = validated_data.get("Estatus",instance.Estatus)
        instance.save()
        paradasdatas = self.context['request'].data.get('paradas','[]')
        for data in paradasdatas:
            if(data.get('id')==""):
                id_ = int(data.get('Id_localidad').get('id')) 
                localidad_objeto = Localidad.objects.get(id=id_)
                del data['Id_localidad']
                parada = Paradas.objects.create(id_ruta=instance,Id_localidad=localidad_objeto)
            else:
                actudata = Paradas.objects.get(id=int(data.get('id')))
                actudata.Id_localidad = Localidad.objects.get(id=data.get('Id_localidad').get('id'))
                actudata.save()
        return instance

class RutaVehiculosSerializer(serializers.ModelSerializer):  
    id_ruta = RutaSerializer(read_only=True)
    class Meta:
        model = Ruta_Vehiculos
        fields = ['id_vehiculos','id_ruta']

    def create(self, validated_data):
        vehiculoObjeto = validated_data.get('id_vehiculos')
        if Ruta_Vehiculos.objects.filter(id_vehiculos=vehiculoObjeto).exists():
            instance = Ruta_Vehiculos.objects.get(id_vehiculos=vehiculoObjeto)
            instance.delete()
        rutaObjeto = Ruta.objects.get(id=self.context['request'].data.get('id_ruta',''))
        create = Ruta_Vehiculos.objects.create(id_ruta=rutaObjeto,id_vehiculos=vehiculoObjeto)
        return create

class VehiculosSerializer(serializers.ModelSerializer):
    ruta = serializers.SerializerMethodField('get_Ruta')
    class Meta:
        model = Vehiculos
        fields = ['id','Nombre','Ubicacion_actual_lat','Ubicacion_actual_long','Consumo_combustible','Distancia_recorrida','Combustible_consumido','ruta']
    
    def get_Ruta(self,obj):
        vehiculo = obj
        queryset = Ruta_Vehiculos.objects.filter(id_vehiculos=vehiculo).all()
        serializer = RutaVehiculosSerializer(queryset,many=True)
        return serializer.data
