from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:post_id>/', views.show_post, name='show_post'),
]