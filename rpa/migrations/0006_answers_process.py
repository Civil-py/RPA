# Generated by Django 5.2 on 2025-04-23 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpa', '0005_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rpa.process'),
        ),
    ]
