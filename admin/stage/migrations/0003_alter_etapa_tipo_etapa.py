# Generated by Django 3.2 on 2022-03-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0002_etapa_tipo_etapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='tipo_etapa',
            field=models.CharField(choices=[('REC', 'RECEPCION'), ('EXT', 'EXTENCION'), ('OTO', 'OTORGAMIENTO'), ('AUT', 'AUTORIZACION')], max_length=3),
        ),
    ]