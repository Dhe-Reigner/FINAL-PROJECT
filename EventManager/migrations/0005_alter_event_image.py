# Generated by Django 5.1.3 on 2024-11-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0004_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
