# Generated by Django 3.2 on 2022-03-20 01:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0006_alter_repartoetapa_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacionetapa',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 20, 3, 44, 533519), verbose_name='Fecha-Hora-Observacion'),
        ),
        migrations.AlterField(
            model_name='observacionetapa',
            name='reparto_etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage.repartoetapa', verbose_name='Reparto-Etapa'),
        ),
    ]