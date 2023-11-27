from django.db.models import Q, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from videos.models import Video


def index(request):
    new_videos = Video.objects.filter(visibilty="public").order_by("-date")[:5]
    liked_videos = Video.objects.filter(visibilty="public").order_by("-date")
    favorite_videos = Video.objects.filter(visibilty="public").order_by("-date")
    pepolar_videos = Video.objects.filter(visibilty="public").annotate(likes_count=Count("likes")).order_by("-likes_count")[:5]
    context = {
        "new_videos": new_videos,
        "pepolar_videos": pepolar_videos
    }
    return render(request, 'index.html', context)
    # return HttpResponse(videos)


def homepage(request):
    return render(request, 'test_temp/index.html')


def contact(request):
    return render(request, 'test_temp/contact.html')


def about(request):
    return render(request, 'test_temp/about.html')


# //Search Page
def search(request):
    query = request.GET.get('q')
    videos = Video.objects.filter(visibilty="public").order_by("-date")
    if query:
        videos = videos.filter(Q(title__icontains=query) | Q(title__icontains=query)).distinct()

    context = {
        "q": query,
        "videos": videos
    }

    return render(request, "search.html", context)


def tags_videos(request, tag_slug=None):
    videos = Video.objects.filter(visibilty="public").order_by("-date")
    tag = None
    if tag_slug is not None:
        tag = get_object_or_404(Tag, slug=tag_slug)
        videos = videos.filter(tags__in=[tag])
    context = {
        "videos": videos,
        "tag": tag
    }

    return render(request, "tags_videos.html", context)


def search_ajax(request):
    query = request.POST.word
    videos = Video.objects.filter(visibilty="public").order_by("-date")
    if query:
        videos = videos.filter(Q(title__icontains=query) | Q(title__icontains=query)).distinct()
    context = {
        "query": query,
        "videos": videos
    }

    return JsonResponse({
        "status": "success",
        "data": context
    })