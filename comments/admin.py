from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from channels.models import Community
from .models import Comment, CommunityComment


class CommentAdmin(ImportExportModelAdmin):
    list_display = ('comment', 'user', 'video', 'active', 'date')


admin.site.register(Comment, CommentAdmin)


class CommunityCommentsAdmin(ImportExportModelAdmin):
    list_display = ('comment', 'user', 'community_post', 'active', 'date')


admin.site.register(CommunityComment, CommunityCommentsAdmin)
