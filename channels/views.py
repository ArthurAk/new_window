from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from channels.forms import CommunityPostForm
from channels.models import Channel, Community
from comments.models import CommunityComment
from videos.models import Video


def index(request):
    channels = Channel.objects.all()
    return render(request, 'channels/index.html', {"channels": channels})


def show(request, channel_id):
    # channels = Channel.objects.get(id=channel_id)
    channel = get_object_or_404(Channel, id=channel_id)
    # videos = Video.objects.filter(user=channel.user, visibilty="public").order_by("views")
    videos = Video.objects.filter(user=channel.user, visibilty="public").order_by("-views")

    try:
        video_features = Video.objects.get(user=channel.user, featured=True)
    except:
        # video_features = None
        video_features = Video.objects.filter(user=channel.user, featured=True).first()
        # messages.warning(request, f"Only One Video Can Be Featured!")

    # return HttpResponse(channel)
    return render(request, 'channels/channel.html',
                  {"channel": channel, "videos": videos, "video_features": video_features})


def show_videos(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    videos = Video.objects.filter(user=channel.user, visibilty="public").order_by("-date")

    return render(request, 'channels/channel-videos.html', {"channel": channel, "videos": videos})


def show_about(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    return render(request, 'channels/channel-about.html', {"channel": channel})


def index_community_posts(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    community_posts = Community.objects.filter(channel=channel, status="active")
    context = {
        "channel": channel,
        "community_posts": community_posts
    }
    return render(request, "channels/channel-community.html", context)


def show_community_post(request, channel_id, community_id):
    community_post = Community.objects.get(id=community_id)
    community_post_comments = CommunityComment.objects.filter(community_post=community_post, active=True).order_by(
        "-date")
    channel = get_object_or_404(Channel, id=channel_id)
    # channel = community_post.channel
    context = {
        "channel": channel,
        "community_post": community_post,
        "community_post_comments": community_post_comments
    }
    return render(request, "channels/channel-community-detail.html", context)


@login_required
def create_community_post(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    if request.user != channel.user:
        messages.success(request, "Post Created!")
        return redirect('channels.show', channel.id)
    if request.method == "POST":
        forms = CommunityPostForm(request.POST, request.FILES)
        if forms.is_valid():
            new_post = forms.save(commit=False)
            new_post.channel = channel
            new_post.save()
            messages.success(request, "Post Created!")
            return redirect("channels.show_community_post", channel_id, new_post.id)
    else:
        forms = CommunityPostForm()
        # return HttpResponse(forms)

    return render(request, "channels/create-post.html", {"forms": forms})


@login_required
def edit_community_post(request, channel_id, community_id):
    channel = Channel.objects.get(id=channel_id)
    community = Community.objects.get(id=community_id)
    user = request.user
    if user != community.channel.user:
        messages.success(request, "You are not allowed to edit this!")
        return redirect('channels.show', channel.id)
    if request.method == "POST":
        form = CommunityPostForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.channel = channel
            edited_post.save()
            messages.success(request, "Post Edited!")
            return redirect("channels.show_community_post", channel.id, community_id)
    else:
        forms = CommunityPostForm(instance=community)

    return render(request, "channels/create-post.html",{"forms": forms})


@login_required
def delete_community_post(request, channel_id, community_id):
    channel = Channel.objects.get(id=channel_id)
    community = Community.objects.get(id=community_id)
    community.delete()
    messages.success(request, "Post Deleted!")
    return redirect(request, "channels.index_community_posts", channel.id)


@login_required
def create_community_comment(request, community_id):
    if request.method == "POST":
        community_post = get_object_or_404(Community, id=community_id)
        comment = request.POST.get("comment")
        user = request.user

        new_comment = CommunityComment.objects.create(comment=comment, user=user, community_post=community_post)
        new_comment.save()
        messages.success(request, "Comment successfully added")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def delete_community_comment(request, community_id, comment_id):
    community_post = Community.objects.get(id=community_id)
    comment = CommunityComment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, f"Comment Deleted.")

    return redirect("channels.show_community_post", community_post.channel.id, community_post.id)


def load_channel_subscribers(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    subs_lists = list(channel.subscribers.values())
    # subs_lists = channel.subscribers.values_list("id", flat=True)
    # subs_lists = channel.subscribers.all().count()
    # return HttpResponse(subs_lists)
    return JsonResponse(subs_lists, safe=False, status=200)


def add_subscriber(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    user = request.user

    if user in channel.subscribers.all():
        channel.subscribers.remove(user)
        response = "Subscribe"
        return JsonResponse(response, safe=False, status=200)
    else:
        channel.subscribers.add(user)
        response = "UnSubscribe"
        return JsonResponse(response, safe=False, status=200)
