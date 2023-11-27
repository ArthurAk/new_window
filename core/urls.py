from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('videos/tags/<slug:tag_slug>', views.tags_videos, name='tags_videos')
    # Temp
    # path('search/', views.index, name='search'),
    # path('upload-video/', views.index, name='upload-video')

]
