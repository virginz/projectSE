# Generated by Django 3.1.3 on 2020-12-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20201211_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='disponibilita',
        ),
        migrations.AddField(
            model_name='availability',
            name='maintainer',
            field=models.ManyToManyField(limit_choices_to={'user_type': 'Maintainer'}, to='portal.Profile'),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]
