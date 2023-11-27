from django.db import models
from taggit.managers import TaggableManager
# from users.models import User
from core.models import user_directory_path
from django.conf import settings


# User = settings.AUTH_USER_MODEL

def get_visibility_values():
    return (
        ('private', 'Private'),
        ('unlisted', 'Unlisted'),
        ('members_only', 'Members Only'),
        ('public', 'Public')
    )


User = settings.AUTH_USER_MODEL


class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    visibilty = models.CharField(choices=get_visibility_values(), default="public", max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    likes = models.ManyToManyField(User, related_name="likes")
    views = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
