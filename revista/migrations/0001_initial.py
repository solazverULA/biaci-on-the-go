# Generated by Django 2.0.5 on 2018-05-29 06:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EjemplarRevista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejemplar', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='Formato de ejemplar incorrecto, ej: e1', regex='^[e]{1}[0-9]{1,3}$')])),
                ('estado', models.CharField(blank=True, choices=[('P', 'Prestado'), ('D', 'Disponible'), ('B', 'Bloqueado')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('cota', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('anio', models.PositiveSmallIntegerField()),
                ('lugar_publicacion', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=1000)),
                ('numero', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=30)),
                ('biblioteca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Biblioteca')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Idioma')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplarrevista',
            name='revista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='revista.Revista'),
        ),
        migrations.AlterUniqueTogether(
            name='ejemplarrevista',
            unique_together={('ejemplar', 'revista')},
        ),
    ]
