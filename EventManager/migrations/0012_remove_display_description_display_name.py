# Generated by Django 5.1.3 on 2024-11-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0011_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='display',
            name='description',
        ),
        migrations.AddField(
            model_name='display',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
