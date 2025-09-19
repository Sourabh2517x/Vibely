
from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.PostCreationView, name="post"),
    path('<str:username>/', views.user_posts, name='user_posts'),
] 