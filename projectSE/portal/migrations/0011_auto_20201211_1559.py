# Generated by Django 3.0.6 on 2020-12-11 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competence',
            name='listTask',
        ),
        migrations.AddField(
            model_name='availability',
            name='week',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(52), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='availability',
            name='day',
            field=models.CharField(choices=[('Lunedì', 'Lunedì'), ('Martedì', 'Martedì'), ('Mercoledì', 'Mercoledì'), ('Giovedì', 'Giovedì'), ('Venerdì', 'Venerdì'), ('Sabato', 'Sabato'), ('Domenica', 'Domenica')], max_length=20),
        ),
    ]
