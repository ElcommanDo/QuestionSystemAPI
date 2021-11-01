from django.urls import path
from .views import *
urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetailsView.as_view(), name='question'),
    path('questions/<slug:slug>/answer/', AnswerListView.as_view(), name='answer'),
    # path('answers/<int:pk>/', AnswerDetailsView.as_view(), name='answer'),
    path('questions/<slug:slug>/answers/', QuestionAnswerList.as_view(), name='answers'),
    path('answer/<int:pk>/', AnswerLike.as_view(), name='votes'),

]

