# Generated by Django 5.0.4 on 2024-05-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
