# Generated by Django 3.0.9 on 2020-08-17 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': 'created', 'ordering': ['-created', '-modified']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Date time on which the object was created.', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
