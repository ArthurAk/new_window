from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Video


class VideoAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "date")


admin.site.register(Video, VideoAdmin)

