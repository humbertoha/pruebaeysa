# Generated by Django 4.0.2 on 2022-05-08 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paradas',
            name='Id_localidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.localidad'),
            preserve_default=False,
        ),
    ]
