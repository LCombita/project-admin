# Generated by Django 3.2 on 2022-04-06 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0016_auto_20220405_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacionetapa',
            name='usuario',
        ),
    ]
