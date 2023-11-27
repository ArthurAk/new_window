from django.db import models


def user_directory_path(instance, filename):
    # return f"user_{instance.user.id}/{filename}"
    return "user_{0}/{1}".format(instance.user.id, filename)
