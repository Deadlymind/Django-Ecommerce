# Generated by Django 4.2 on 2023-12-19 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_image_brand_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='images',
            new_name='image',
        ),
    ]