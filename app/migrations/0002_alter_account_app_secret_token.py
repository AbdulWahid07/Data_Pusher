# Generated by Django 5.0.2 on 2024-02-21 08:24

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='app_secret_token',
            field=models.CharField(default=app.models.generate_secret_token, max_length=255, unique=True),
        ),
    ]
