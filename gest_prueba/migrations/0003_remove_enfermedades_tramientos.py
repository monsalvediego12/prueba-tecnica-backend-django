# Generated by Django 5.0.6 on 2024-06-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gest_prueba', '0002_enfermedades_tratamientos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfermedades',
            name='tramientos',
        ),
    ]
