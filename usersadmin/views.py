from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from videos.models import Video


@login_required
def stadio(request):
    user = request.user
    channel = user.channel
    videos = Video.objects.filter(user=user)

    context = {
        "user": user,
        "channel": channel,
        "videos": videos
    }

    return render(request, "usersadmin/index.html", context)
