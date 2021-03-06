# Generated by Django 4.0.2 on 2022-05-07 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250)),
                ('Estatus', models.BooleanField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250)),
                ('Ubicacion_actual_lat', models.FloatField()),
                ('Ubicacion_actual_long', models.FloatField()),
                ('Consumo_combustible', models.PositiveIntegerField()),
                ('Distancia_recorrida', models.FloatField()),
                ('Combustible_consumido', models.FloatField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('Longitud', models.FloatField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
                ('activa', models.BooleanField()),
                ('id_ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.IntegerField()),
                ('Nombre', models.CharField(max_length=250)),
                ('Id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.IntegerField()),
                ('Nombre', models.CharField(max_length=250)),
                ('Latitud', models.FloatField()),
                ('Longitud', models.FloatField()),
                ('Id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.estado')),
                ('Id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.municipio')),
            ],
        ),
        migrations.AddConstraint(
            model_name='municipio',
            constraint=models.UniqueConstraint(fields=('id', 'Id_estado'), name='unique_municipio'),
        ),
        migrations.AddConstraint(
            model_name='localidad',
            constraint=models.UniqueConstraint(fields=('id', 'Id_estado', 'Id_municipio'), name='unique_localidad'),
        ),
    ]
