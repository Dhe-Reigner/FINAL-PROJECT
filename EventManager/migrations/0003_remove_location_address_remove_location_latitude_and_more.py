# Generated by Django 5.1.3 on 2024-12-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0002_display_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
    ]
