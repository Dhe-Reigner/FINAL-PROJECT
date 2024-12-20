# Generated by Django 5.1.3 on 2024-12-04 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventSalesSystem', '0002_affiliate_content_email_influencer_mobile_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='affiliate',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='influencer',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='mobile',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='social',
            old_name='image',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='image',
            new_name='preview',
        ),
    ]
