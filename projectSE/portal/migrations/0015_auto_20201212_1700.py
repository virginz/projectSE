# Generated by Django 3.1.3 on 2020-12-12 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20201212_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='maintainer',
        ),
        migrations.AddField(
            model_name='availability',
            name='maintainer',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'Maintainer'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.profile'),
        ),
    ]
