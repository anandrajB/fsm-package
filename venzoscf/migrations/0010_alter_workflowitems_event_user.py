# Generated by Django 3.2.5 on 2022-07-12 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venzoscf', '0009_alter_workflowitems_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowitems',
            name='event_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
