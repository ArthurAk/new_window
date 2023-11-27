from django.urls import path
from . import views


urlpatterns = [
    path('auth/sign-up/', views.register_view, name='auth.register'),
    path('auth/login/', views.login_view, name='auth.login'),
    path('auth/logout/', views.logout_view, name='auth.logout'),
    path('<int:user_id>/profile/subscribtions/', views.show_subscribtions, name='show_user_subscribtions')
]
