# Generated by Django 3.0.6 on 2020-11-25 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_auto_20201124_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('SystemAdministrator', 'SystemAdministrator'), ('Planner', 'Planner'), ('Maintainer', 'Maintainer')], max_length=20)),
                ('competences', models.ManyToManyField(blank=True, null=True, to='portal.Competences')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]
