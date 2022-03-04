# Generated by Django 3.2 on 2022-03-04 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActoJuridico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_acto', models.CharField(max_length=100, unique=True, verbose_name='Acto Jurídico')),
            ],
            options={
                'verbose_name': 'Acto Jurídico',
                'verbose_name_plural': 'Actos Jurídicos',
            },
        ),
        migrations.CreateModel(
            name='Reparto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha_reparto', models.DateField(help_text='Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.', verbose_name='Fecha Reparto')),
                ('escritura', models.CharField(blank=True, max_length=5, null=True, verbose_name='Número Escritura')),
                ('fecha_escritura', models.DateField(blank=True, help_text='Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.', null=True, verbose_name='Fecha Escritura')),
                ('hoja_ruta', models.CharField(blank=True, max_length=20, null=True)),
                ('anio_escritura', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('activo', models.BooleanField(default=True, verbose_name='Reparto Activo')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('editado', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
                ('acto_juridico', models.ManyToManyField(db_index=True, related_name='acto_juridico', to='deed.ActoJuridico', verbose_name='Acto Jurídico')),
                ('protocolista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Asistente Escrituración')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.proyecto', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Hoja de Ruta',
                'verbose_name_plural': 'Hojas de Ruta',
            },
        ),
        migrations.CreateModel(
            name='OtorganteReparto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(max_length=20, verbose_name='Número Factura')),
                ('derechos_notariales', models.DecimalField(decimal_places=1, max_digits=9, verbose_name='Derechos Notariales')),
                ('valor_registro', models.DecimalField(decimal_places=1, max_digits=9, verbose_name='Registro')),
                ('valor_rentas', models.DecimalField(decimal_places=1, max_digits=9, verbose_name='Rentas')),
                ('canje', models.BooleanField(default=False, verbose_name='Para Canje')),
                ('otorgante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Otorgante')),
                ('reparto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deed.reparto', verbose_name='Reparto')),
            ],
            options={
                'verbose_name': 'Otorgante',
                'verbose_name_plural': 'Otorgantes',
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmueble', models.CharField(help_text='Describa qué tipo de inmueble es.', max_length=150, verbose_name='Inmueble')),
                ('matricula', models.CharField(help_text='Ingrese el número de matrícula completo', max_length=150, verbose_name='Matricula Inmobiliaria')),
                ('reparto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deed.reparto', verbose_name='Reparto')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
            },
        ),
    ]
