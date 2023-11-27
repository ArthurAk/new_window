# Generated by Django 4.2.7 on 2023-11-11 21:07

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('disabled', 'Disabled')], default='active', max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('keywords', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('subscribers', models.ManyToManyField(related_name='user_subscribers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]