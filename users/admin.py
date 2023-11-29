from django.contrib import admin
from .models import User, Profile, Group, Permission
from import_export.admin import ImportExportModelAdmin


class PermissionAdmin(ImportExportModelAdmin):
    list_display = ("codename", "name")


class GroupAdmin(ImportExportModelAdmin):
    list_display = ("name", "description")


class UserAdmin(ImportExportModelAdmin):
    list_display = ("username", "email", "last_name")


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Permission, PermissionAdmin)



class ProfileAdmin(ImportExportModelAdmin):
    list_display = ["user",]


admin.site.register(Profile, ProfileAdmin)
