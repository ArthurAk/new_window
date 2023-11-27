from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Channel, Community


class ChannelAdmin(ImportExportModelAdmin):
    # list_display = ('channel_name', 'fullname', 'subscribers_count')
    list_display = ('channel_name', 'full_name', 'user', 'status')


admin.site.register(Channel, ChannelAdmin)


class CommunityAdmin(ImportExportModelAdmin):
    list_display = ('title', "channel", "status")


admin.site.register(Community, CommunityAdmin)
