# Generated by Django 5.1.3 on 2024-11-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0002_alter_event_end_date_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='m1.jpg', upload_to=''),
        ),
    ]
