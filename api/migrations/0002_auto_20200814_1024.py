# Generated by Django 3.0.9 on 2020-08-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='generos',
            field=models.ManyToManyField(to='api.Genero'),
        ),
        migrations.AddField(
            model_name='series',
            name='generos',
            field=models.ManyToManyField(to='api.Genero'),
        ),
    ]
