# Generated by Django 4.2 on 2024-01-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_settings_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
