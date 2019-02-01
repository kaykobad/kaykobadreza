from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tutorials, name='tutorials'),
    path('<tutname>/', views.tut_details, name='tut_intro'),
    path('<tutname>/<int:chapter>/', views.tut_details, name='tut_details'),
]
