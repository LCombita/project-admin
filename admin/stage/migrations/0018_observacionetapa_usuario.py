# Generated by Django 3.2 on 2022-04-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0017_remove_observacionetapa_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacionetapa',
            name='usuario',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Usuario'),
        ),
    ]