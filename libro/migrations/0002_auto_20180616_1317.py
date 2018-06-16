# Generated by Django 2.0.5 on 2018-06-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='vista',
            field=models.ImageField(default='/images/default.png', null=True, upload_to='libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='url',
            field=models.URLField(),
        ),
    ]
