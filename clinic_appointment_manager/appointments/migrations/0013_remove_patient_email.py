# Generated by Django 5.0.4 on 2024-05-04 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_remove_patient_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]
