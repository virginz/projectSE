# Generated by Django 3.1.3 on 2020-12-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20201212_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='competences_needed',
            field=models.ManyToManyField(blank=True, null=True, to='portal.Competence'),
        ),
    ]
