# Generated by Django 4.1.1 on 2022-09-09 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_location_alter_category_options_ad_category_ad_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
    ]
