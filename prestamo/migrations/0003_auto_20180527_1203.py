# Generated by Django 2.0.5 on 2018-05-27 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0002_auto_20180527_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 27, 12, 3, 26, 611075)),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 27, 12, 3, 26, 611028)),
        ),
    ]