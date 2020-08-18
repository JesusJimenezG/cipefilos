# Generated by Django 3.0.9 on 2020-08-18 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=150)),
                ('imagen', models.URLField(default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png', help_text='De imdb mismo')),
                ('nacimiento', models.DateField()),
                ('actores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Actores')),
            ],
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='actores',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='director',
        ),
        migrations.RemoveField(
            model_name='series',
            name='actores',
        ),
        migrations.RemoveField(
            model_name='series',
            name='director',
        ),
        migrations.DeleteModel(
            name='Casting',
        ),
        migrations.DeleteModel(
            name='Directores',
        ),
        migrations.AddField(
            model_name='reparto',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pelicula'),
        ),
        migrations.AddField(
            model_name='actores',
            name='peliculas',
            field=models.ManyToManyField(through='api.Reparto', to='api.Pelicula'),
        ),
    ]