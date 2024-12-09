# Generated by Django 5.1.3 on 2024-12-08 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0009_rename_description_movie_description3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='location',
            field=models.ForeignKey(blank=True, default='', max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='EventManager.location'),
        ),
    ]