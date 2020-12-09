# Generated by Django 3.1.3 on 2020-12-09 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot8_9', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot9_10', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot10_11', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot11_12', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot14_15', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot15_16', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('slot16_17', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)])),
                ('day', models.DateField()),
                ('maintainer', models.ManyToManyField(limit_choices_to={'user_type': 'Maintainer'}, to='portal.Profile')),
            ],
        ),
    ]
