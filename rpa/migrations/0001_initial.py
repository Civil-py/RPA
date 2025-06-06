# Generated by Django 5.2 on 2025-04-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qone', models.CharField(choices=[('Have not estimated the repetitions', 'A'), ('Very little repetitive tasks required', 'B'), ('Some repetitive tasks required', 'C'), ('Many repetitive tasks required', 'D'), ('Extensive repetitive tasks required', 'E')], max_length=64, null=True)),
                ('Qtwo', models.CharField(choices=[('Not sure of the status or health of the process', 'A'), ('Some of the process is currently executed in business', 'B'), ('New process is required altogether', 'C'), ('Enhancement to existing process is required', 'D'), ('Entire process is currently executed in business', 'E')], max_length=64, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
