from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
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
    return render(request, 'usersadmin/users/index_users.html', {'users': users})


def index_groups(request):

    groups = Group.objects.all
    return render(request, 'usersadmin/groups/index_groups.html', {'groups': groups})


def show_group(request, group_id):
    group = Group.objects.get(id=group_id)
    permissions = group.permissions.all()
    context = {
        'group': group,
        'permissions': permissions
    }
    return render(request, 'usersadmin/groups/show_group.html', context)


def edit_group(request, group_id):
    if request.method == 'POST':
        # return HttpResponse(group_id)
        group = Group.objects.get(id=group_id)
        name = request.POST.get('name')
        # permission_exists = Permission.objects.filter(codename=codename)
        # if permission_exists:
        #     messages.warning(request, "permission already exists")
        #     return render(request, "usersadmin/groups/create_group.html", {"message": messages})
        # group.update(name=name, codename=codename)
        group.name = name
        group.save()
        return render(request, 'usersadmin/groups/index_groups.html', {'group': group})
    else:
        group = Group.objects.get(id=group_id)
        return render(request, 'usersadmin/groups/edit_group.html', {'group': group})


def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group_exists = Group.objects.filter(name=name)
        if group_exists:
            messages.warning(request, "group already exists")
            return render(request, "usersadmin/groups/create_group.html", {"message": messages})
        group = Group.objects.create(name=name)
        group.save()
        return render(request, 'usersadmin/groups/index_groups.html', group)
    else:
        return render(request, 'usersadmin/groups/create_group.html')


def create_permission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        codename = request.POST.get('codename')
        permission_exists = Permission.objects.filter(codename=codename)
        if permission_exists:
            messages.warning(request, "permission already exists")
            return render(request, "usersadmin/groups/create_permission.html", {"message": messages})
        permission = Permission.objects.create(codename=codename)
        permission.save()
        return render(request, 'usersadmin/groups/index_permissions.html', permission)
    else:
        return render(request, 'usersadmin/groups/create_permission.html')
