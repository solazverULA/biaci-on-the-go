# Generated by Django 2.0.5 on 2018-05-22 01:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=80)),
                ('cuidad', models.CharField(max_length=80)),
                ('avenida', models.CharField(max_length=80)),
                ('calle', models.CharField(max_length=80)),
                ('edificio', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, choices=[('P', 'Prestado'), ('D', 'Disponible'), ('B', 'Bloqueado')], default='D', max_length=1)),
                ('biblioteca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('cota', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('anio', models.PositiveSmallIntegerField()),
                ('lugar_publicacion', models.TextField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('descripcion', models.TextField(max_length=1000)),
                ('autor', models.ManyToManyField(to='libro.Autor')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='materia',
            field=models.ManyToManyField(to='libro.Materia'),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Libro'),
        ),
    ]
