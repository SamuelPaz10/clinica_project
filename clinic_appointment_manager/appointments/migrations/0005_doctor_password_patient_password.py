# Generated by Django 5.0.4 on 2024-05-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_delete_available_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='1234', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='1234', max_length=50),
        ),
    ]