# Generated by Django 4.2 on 2024-01-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='settings')),
                ('subtitle', models.TextField(max_length=500)),
                ('call_us', models.CharField(max_length=25)),
                ('email_us', models.CharField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('phones', models.TextField(max_length=50)),
                ('adress', models.TextField(max_length=100)),
                ('android_app', models.URLField(blank=True, null=True)),
                ('ios_app', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
