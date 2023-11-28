from django.urls import path
from . import views


urlpatterns = [
    path('', views.stadio, name='stadio'),
    path('users/', views.index_users, name='stadio.index_users'),
    path('groups/', views.index_groups, name='stadio.index_groups'),
    path('groups/<int:group_id>/', views.show_group, name='stadio.show_group'),
    path('groups/create/', views.create_group, name='stadio.create_group'),
    path('groups/edit/<int:group_id>/', views.edit_group, name='stadio.edit_group'),
    path('groups/<int:group_id>/permissions', views.create_group, name='stadio.create_group'),

]
