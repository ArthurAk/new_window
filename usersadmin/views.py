from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

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


@login_required()
def index_users(request):

    users = get_user_model().objects.all
    return render(request, 'usersadmin/index_users.html', {'users': users})


def index_groups(request):

    groups = Group.objects.all
    return render(request, 'usersadmin/index_groups.html', {'groups': groups})


def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group_exists = Group.objects.filter(name=name)
        if group_exists:
            messages.warning(request, "group already exists")
            return render(request, "usersadmin/create_group.html", {"message": messages})
        group = Group.objects.create(name=name)
        return redirect('usersadmin/index')
    else:
        return render(request, 'usersadmin/create_group.html')


