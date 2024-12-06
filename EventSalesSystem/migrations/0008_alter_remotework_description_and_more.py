# Generated by Django 5.1.3 on 2024-12-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventSalesSystem', '0007_remove_remotework_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotework',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='remotework',
            name='work_schedule',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
