# Generated by Django 4.2 on 2024-01-16 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_cart_total_cart_total_with_coupon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='star_date',
            new_name='start_date',
        ),
    ]
