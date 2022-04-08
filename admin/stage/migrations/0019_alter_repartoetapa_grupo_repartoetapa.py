# Generated by Django 3.2 on 2022-04-08 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0018_observacionetapa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartoetapa',
            name='grupo_repartoetapa',
            field=models.CharField(choices=[('NIN', 'NINGUNO'), ('FAC', 'FACTURACION'), ('FIN', 'FINALIZACION'), ('JUR', 'JURIDICA'), ('PRO', 'PROCOTOLISTA')], default='NIN', max_length=3),
        ),
    ]
