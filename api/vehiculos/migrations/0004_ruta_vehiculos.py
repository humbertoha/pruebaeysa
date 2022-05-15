# Generated by Django 4.0.2 on 2022-05-15 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_remove_paradas_longitud_remove_paradas_activa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta_Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculos')),
                ('id_vehiculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.ruta')),
            ],
        ),
    ]
