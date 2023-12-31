from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.models import Group, Permission
from usersadmin.forms import PermissionForm
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


def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        group_exists = Group.objects.filter(name=name)
        if group_exists:
            messages.warning(request, "group already exists")
            return render(request, "usersadmin/groups/create_group.html", {"message": messages})
        group = Group.objects.create(name=name, description=description)
        group.save()
        return render(request, 'usersadmin/groups/index_groups.html', {'group': group})
    else:
        return render(request, 'usersadmin/groups/create_group.html')


def edit_group(request, group_id):
    if request.method == 'POST':
        group = Group.objects.get(id=group_id)
        name = request.POST.get('name')
        description = request.POST.get('description')
        permissions = request.POST.getlist('permissions')
        # return HttpResponse(permissions)
        # permission_exists = Permission.objects.filter(codename=codename)
        # if permission_exists:
        #     messages.warning(request, "permission already exists")
        #     return render(request, "usersadmin/groups/create_group.html", {"message": messages})
        # group.update(name=name, codename=codename)
        group.name = name
        group.description = description
        for item in permissions:
            permission = Permission.objects.get(codename=item)
            group.permissions.add(permission)
        group.save()
        return redirect("stadio.index_groups", group)
    else:
        group = Group.objects.get(id=group_id)
        permissions = Permission.objects.all()
        context = {
            'group': group,
            'permissions': permissions
        }
        return render(request, 'usersadmin/groups/edit_group.html', context)


def index_permissions(request):
    permissions = Permission.objects.all()
    return render(request, 'usersadmin/groups/index_permissions.html', {'permissions': permissions})


def show_permission(request, permission_id):
    pass


def create_permission(request):
    if request.method == 'POST':
        forms = PermissionForm(request.POST)
        if forms.is_valid():
            forms.save(commit=False)
            forms.save()
            messages.success(request, 'Permission created successfully!')
            return redirect("stadio.index_permissions", forms.name)
    else:
        forms = PermissionForm()
        return render(request, 'usersadmin/groups/create_permission.html',{'forms': forms})


def edit_permission(request, permission_id):
    pass
