from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

from videos.models import user_directory_path

User = settings.AUTH_USER_MODEL
user_path = user_directory_path

STATUS = (
    ("active", "Active"),
    ("disabled", "Disabled")
)


class Channel(models.Model):
    channel_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200, null=True)
    banner = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    channel_art = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50, default="active")
    verified = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    business_email = models.EmailField(null=True, blank=True)
    make_business_email_public = models.BooleanField(default=True)
    business_location = models.TextField(null=True, blank=True)
    make_business_location_public = models.BooleanField(default=False)
    total_views = models.IntegerField(default=0)
    website = models.URLField(null=True)
    instagram = models.URLField(null=True)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)

    keywords = TaggableManager()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="channel")
    subscribers = models.ManyToManyField(User, related_name="user_subscribers")

    def __str__(self):
        return self.channel_name


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.channel.user.id, filename)


class Community(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50, default="active")
    date = models.DateTimeField(auto_now_add=True)

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Community Posts"
