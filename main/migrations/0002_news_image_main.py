# Generated by Django 5.0.6 on 2024-05-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]
