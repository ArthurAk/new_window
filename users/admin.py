from django.contrib import admin
from .models import User, Profile
from import_export.admin import ImportExportModelAdmin


class UserAdmin(ImportExportModelAdmin):
    list_display = ("username", "email", "last_name")


admin.site.register(User, UserAdmin)


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ["user",]


admin.site.register(Profile, ProfileAdmin)
