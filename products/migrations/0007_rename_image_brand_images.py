# Generated by Django 4.2 on 2023-12-23 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_images_brand_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='image',
            new_name='images',
        ),
    ]
