# Generated by Django 3.0.9 on 2020-08-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200817_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actores',
            name='peliculas',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='equipo',
            field=models.ManyToManyField(through='api.Reparto', to='api.Actores'),
        ),
    ]
