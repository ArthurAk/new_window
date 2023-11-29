from django.contrib.auth.models import AbstractUser
from django.db import models

from channels.models import Channel
from videos.models import Video


class Permission(models.Model):
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    permissions = models.ManyToManyField(Permission, related_name='groups')

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=1000, unique=True)
    user_groups = models.ManyToManyField(Group, related_name='group_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    saved_videos = models.ManyToManyField(Video, related_name="saved_videos")

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # instance user save its profile


models.signals.post_save.connect(create_user_profile, sender=User)
models.signals.post_save.connect(save_user_profile, sender=User)


def create_user_channel(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance, channel_name=instance.username)


def save_user_channel(sender, instance, **kwargs):
    instance.channel.save()


models.signals.post_save.connect(create_user_channel, sender=User)
models.signals.post_save.connect(save_user_channel, sender=User)
