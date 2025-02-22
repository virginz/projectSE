# Generated by Django 3.1.3 on 2020-12-15 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20201212_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='slot10_11',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot11_12',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot14_15',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot15_16',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot16_17',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot8_9',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='slot9_10',
        ),
        migrations.AddField(
            model_name='availability',
            name='minutes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='availability',
            name='time_slot',
            field=models.CharField(blank=True, choices=[('8-9', '8-9'), ('9-10', '9-10'), ('10-11', '10-11'), ('11-12', '11-12'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], max_length=20, null=True),
        ),
    ]
