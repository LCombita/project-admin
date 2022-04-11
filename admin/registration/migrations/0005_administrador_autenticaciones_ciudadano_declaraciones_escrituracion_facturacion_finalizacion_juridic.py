# Generated by Django 3.2 on 2022-03-26 01:19

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20220130_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Autenticaciones',
            fields=[
            ],
            options={
                'verbose_name': 'Autenticaciones',
                'verbose_name_plural': 'Autenticaciones',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
            ],
            options={
                'verbose_name': 'Ciudadano',
                'verbose_name_plural': 'Ciudadanos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Declaraciones',
            fields=[
            ],
            options={
                'verbose_name': 'Declaraciones',
                'verbose_name_plural': 'Declaraciones',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Escrituracion',
            fields=[
            ],
            options={
                'verbose_name': 'Escrituracion',
                'verbose_name_plural': 'Asistentes_Escrituracion',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
            ],
            options={
                'verbose_name': 'Facturacion',
                'verbose_name_plural': 'Facturadores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Finalizacion',
            fields=[
            ],
            options={
                'verbose_name': 'Finalizacion',
                'verbose_name_plural': 'Finalizacion',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Juridica',
            fields=[
            ],
            options={
                'verbose_name': 'Juridica',
                'verbose_name_plural': 'Juridica',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reparto',
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
        migrations.CreateModel(
            name='Tramitador',
            fields=[
            ],
            options={
                'verbose_name': 'Tramitador',
                'verbose_name_plural': 'Tramitadores',
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