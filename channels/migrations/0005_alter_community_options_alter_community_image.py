# Generated by Django 4.2.7 on 2023-11-13 06:20

import channels.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0004_community'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': 'Community', 'verbose_name_plural': 'Community Posts'},
        ),
        migrations.AlterField(
            model_name='community',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=channels.models.user_directory_path),
        ),
    ]
