# Generated by Django 4.2.7 on 2023-11-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_permission_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_groups',
            field=models.ManyToManyField(related_name='group_users', to='users.group'),
        ),
    ]
