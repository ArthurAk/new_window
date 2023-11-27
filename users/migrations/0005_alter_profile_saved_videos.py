# Generated by Django 4.2.7 on 2023-11-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_featured'),
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_videos',
            field=models.ManyToManyField(related_name='saved_videos', to='videos.video'),
        ),
    ]
