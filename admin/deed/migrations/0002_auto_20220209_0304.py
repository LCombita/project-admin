# Generated by Django 3.2 on 2022-02-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repartoetapa',
            options={'verbose_name': 'Etapa Hoja Ruta', 'verbose_name_plural': 'Etapas Hoja Ruta'},
        ),
        migrations.RemoveField(
            model_name='reparto',
            name='hoja_ruta',
        ),
        migrations.AlterField(
            model_name='reparto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Hoja Ruta'),
        ),
    ]
