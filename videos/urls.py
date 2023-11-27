from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='videos.index'),
    path('saved/', views.watched_videos_index, name='videos.saved.index'),
    path('liked/', views.liked_videos_index, name='videos.liked.index'),
    path("show/<int:video_id>/", views.show, name='videos.show'),
    path("create/", views.create, name='videos.create'),
    path("edit/<int:video_id>/", views.edit, name='videos.edit'),
    path("send-video-comment-ajax", views.send_comment_ajax, name='videos.send.comment'),
    path("delete-video-comment-ajax", views.delete_comment_ajax, name='videos.delete.comment'),
    path("add-like/<int:video_id>/", views.add_like, name='videos.add-like'),
    path("load-likes/<int:video_id>/", views.show_likes, name='videos.load-likes'),
    path("add-saved/<int:video_id>/", views.add_to_saved, name='videos.add-to-saved')
]
