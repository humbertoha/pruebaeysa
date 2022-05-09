import pandas as pd
import os
from django.db import transaction
from django.core.management.base import BaseCommand
from vehiculos.models import Estado, Municipio,Localidad

class Command(BaseCommand):
    help = "importando test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("eliminando vieja informacion...")
        models = [Estado,Municipio,Localidad]
        for m in models:
            m.truncate()

        self.stdout.write("importando la nueva informacion...")
        # Importando csv AGEMML a base de datos
        csv_filename = os.path.join(os.path.dirname(__file__), 'AGEEML_20224302214353.csv')
        df=pd.read_csv(csv_filename,encoding='unicode_escape',sep=',')
        df_estado = df[["Cve_Ent","Nom_Ent"]].copy() 
        row_iter = df_estado.drop_duplicates().iterrows()
        objs = [
    		Estado(
    			id = row["Cve_Ent"],
    			Nombre = row['Nom_Ent'],
    			)
    		for index, row in row_iter
    	]
        Estado.objects.bulk_create(objs)
        df_mun = df[["Cve_Ent","Cve_Mun","Nom_Mun"]].copy() 
        row_iter = df_mun.drop_duplicates()
        row_iter = row_iter.iterrows()
        objs = [
    		Municipio(
    			municipio = row['Cve_Mun'],
    			Nombre = row['Nom_Mun'],
    			Id_estado = Estado(id=row['Cve_Ent'])
    			)
    		for index, row in row_iter
        ]
        Municipio.objects.bulk_create(objs)
        df_loc = df[["Cve_Ent","Cve_Mun","Cve_Loc","Nom_Loc","Lat_Decimal","Lon_Decimal"]].copy()
        row_iter = df_loc.drop_duplicates().iterrows()
        objs = [
    		Localidad(
    			localidad = row['Cve_Loc'],
    			Nombre = row['Nom_Loc'],
    			Latitud = row["Lat_Decimal"],
				Longitud = row["Lon_Decimal"],
    			Id_municipio = Municipio(id=row['Cve_Mun']),
    			Id_estado = Estado(id=row['Cve_Ent'])
    			)
    		for index, row in row_iter
    	]
        Localidad.objects.bulk_create(objs)