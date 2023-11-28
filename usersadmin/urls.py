from django.urls import path
from . import views


urlpatterns = [
    path('', views.stadio, name='stadio'),
    path('users/', views.index_users, name='stadio.index_users'),
    path('groups/', views.index_groups, name='stadio.index_groups'),
]
