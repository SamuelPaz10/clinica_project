# Generated by Django 5.0.4 on 2024-05-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_remove_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
    ]
