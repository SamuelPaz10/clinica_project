# Generated by Django 5.0.4 on 2024-05-03 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_available_schedule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Available_schedule',
        ),
    ]