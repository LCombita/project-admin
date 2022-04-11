# Generated by Django 3.2 on 2022-03-26 16:40

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_administrador_autenticaciones_ciudadano_declaraciones_escrituracion_facturacion_finalizacion_juridic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reparto',
        ),
        migrations.CreateModel(
            name='RepartoUser',
            fields=[
            ],
            options={
                'verbose_name': 'Reparto',
                'verbose_name_plural': 'Reparto',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]