# Generated by Django 3.2 on 2022-03-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapa',
            name='tipo_etapa',
            field=models.CharField(choices=[('SEL', 'SELECCIONE'), ('REC', 'RECEPCION'), ('EXT', 'EXTENCION'), ('OTO', 'OTORGAMIENTO'), ('AUT', 'AUTORIZACION')], default='SEL', max_length=3),
        ),
    ]
