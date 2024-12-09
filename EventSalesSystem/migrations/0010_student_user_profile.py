# Generated by Django 5.1.3 on 2024-12-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventSalesSystem', '0009_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('full_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Product')),
                ('about', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('job', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, default='', max_length=100, null=True)),
                ('twitter_profile', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('facebook_profile', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('instagram_profile', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('linkedin_profile', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
