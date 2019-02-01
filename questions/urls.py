from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('askquestion/', views.ask_question, name='ask_question'),
    path('<int:question_id>/', views.specific_question, name='specific_question'),
]