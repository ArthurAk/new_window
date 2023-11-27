from django.conf import settings
from django.db import models

from channels.models import Community
from videos.models import Video

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:30]


class CommunityComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="community_comments")
    community_post = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name: "Community Comments"
        verbose_name_plural: "Community Comments"
