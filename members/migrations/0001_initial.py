# Generated by Django 5.1.3 on 2024-12-02 06:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='State')),
                ('zip_code', models.CharField(max_length=10, null=True, verbose_name='Zip Code')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='Country')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='Phone Number')),
                ('website', models.URLField(null=True, verbose_name='Website')),
                ('longitude', models.TextField(max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.TextField(max_length=50, null=True, verbose_name='Latitude')),
                ('captcha_score', models.FloatField(default=0.0)),
                ('has_profile', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
