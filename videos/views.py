from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from channels.forms import CommunityPostForm
from channels.models import Channel
from comments.models import Comment
from users.models import Profile
from .forms import VideoForm
from .models import Video


def index(request):
    # videos = Video.objects.all()
    videos = Video.objects.filter(visibilty='public')

    context = {
        "videos": videos
    }

    return render(request, 'videos/index.html', context)


def history_videos_index(request):
    last_view_videos = Video.objects.filter(visibilty='public').annotate().order_by('')


def liked_videos_index(request):
    videos = Video.objects.filter(visibilty='public')
    liked_videos = videos.filter(likes__in=[request.user])
    context = {
        "videos": liked_videos
    }

    return render(request, 'videos/liked-videos-index.html', context)


def watched_videos_index(request):
    user = request.user
    videos = user.profile.saved_videos.all()

    context = {
        "videos": videos
    }

    return render(request, 'videos/watch-list-index.html', context)


def show(request, video_id):
    video = Video.objects.get(id=video_id)

    # Get Similar Videos
    video_tags_id = video.tags.values_list('id', flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count('tags')).order_by('-same_tags', '-date')[:25]
    # Get Comments of Video
    comments = Comment.objects.filter(active=True, video=video).order_by('-date')
    # return HttpResponse(comments)
    context = {
        "video": video,
        "similar_videos": similar_videos,
        "comments": comments
    }
    video.views = video.views + 1
    video.save()
    channel = video.user.channel
    channel.total_views += 1
    channel.save()
    # return render(request, 'videos/video.html', context)
    # return render(request, 'videos/video.html', {"video": video})
    return render(request, 'videos/video.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # return HttpResponse(request.POST)
            new_video = form.save(commit=False)
            new_video.user = user
            new_video.save()
            form.save_m2m()
            messages.success(request, f"Video Created!")
            return redirect('channels.show', user.channel.id)
        else:
            return HttpResponse(form.errors)

    else:
        forms = VideoForm()
    # return HttpResponse(form)
    return render(request, "videos/create-video.html", {"froms": forms})


@login_required
def edit(request, video_id):
    video = Video.objects.get(id=video_id)
    if request.method == 'POST':
        user = request.user
        video_user = video.user
        if(video_user != user):
            return redirect('channels.show', user.channel.id)

        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            # return HttpResponse(request.POST)
            new_video = form.save(commit=False)
            new_video.user = user
            new_video.save()
            form.save_m2m()
            messages.success(request, f"Video Created!")
            return redirect('channels.show', user.channel.id)
        else:
            return HttpResponse(form.errors)

    else:
        forms = VideoForm(instance=video)
    # return HttpResponse(form)
    return render(request, "videos/create-video.html", {"froms": forms})


# //Ajax Views


def add_like(request, video_id):
    user = request.user
    video = Video.objects.get(id=video_id)
    if user in video.likes.all():
        video.likes.remove(user)
        like_response = "Like"
        return JsonResponse(like_response, safe=False, status=200)
    else:
        video.likes.add(user)
        like_response = "DisLike"
        return JsonResponse(like_response, safe=False, status=200)


def show_likes(request, video_id):
    video = Video.objects.get(id=video_id)
    likes = list(video.likes.values())

    return JsonResponse(likes, safe=False, status=200)


def add_to_saved(request, video_id):
    video = Video.objects.get(id=video_id)
    # return JsonResponse(video)
    profile = request.user.profile
    # profile = Profile.objects.get(user=request.user)

    if video in profile.saved_videos.all():
        profile.saved_videos.remove(video)
        saved_response = "Saved"
        return JsonResponse(saved_response, safe=False, status=200)
    else:
        profile.saved_videos.add(video)
        saved_response = "UnSaved"
        return JsonResponse(saved_response, safe=False, status=200)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER')) TODO:// Whats This Work ?


def send_comment_ajax(request):
    if request.method == 'POST':
        video_id = request.POST.get('video_id')
        video = Video.objects.get(id=video_id)
        user = request.user
        comment = request.POST.get('comment')

        new_comment = Comment.objects.create(user=user, video=video, comment=comment, active=True)
        new_comment.save()
        response = JsonResponse(
            {
                'success': True,
                'comment': comment
            }
        )
        return HttpResponse(response)
    else:
        pass


@csrf_exempt
def delete_comment_ajax(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({
            'success': True,
            'message': 'Comment was deleted'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Get Request was not supported For This Url'
        })
