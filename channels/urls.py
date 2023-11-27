from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='channels.index'),
    path('show/<int:channel_id>/', views.show, name='channels.show'),
    path('add-sub/<int:channel_id>/', views.add_subscriber, name='channels.add_sub'),
    path('load-subs/<int:channel_id>/', views.load_channel_subscribers, name='channels.load_subs'),
    path('<int:channel_id>/show-videos/', views.show_videos, name='channels.show_videos'),
    path('<int:channel_id>/about/', views.show_about, name='channels.show_about'),
    path('<int:channel_id>/community-posts/', views.index_community_posts, name='channels.index_community_posts'),
    path('<int:channel_id>/community-posts/create/', views.create_community_post, name='channels.create_community_post'),
    path('<int:channel_id>/community-posts/detail/<int:community_id>/', views.show_community_post, name='channels.show_community_post'),
    path('<int:channel_id>/community-posts/edit/<int:community_id>/', views.edit_community_post, name='channels.edit_community_post'),
    path('<int:channel_id>/community-posts/delete/<int:community_id>/', views.delete_community_post, name='channels.delete_community_post'),
    path('community-posts/<int:community_id>/create-comment/', views.create_community_comment, name='channels.create_community_comment'),
    path('community-posts/<int:community_id>/delete-comment/<int:comment_id>', views.delete_community_comment, name='channels.delete_community_comment')
]
