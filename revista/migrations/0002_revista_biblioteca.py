# Generated by Django 2.0.5 on 2018-05-29 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revista',
            name='biblioteca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Biblioteca'),
        ),
    ]