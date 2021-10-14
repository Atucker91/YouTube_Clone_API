from django.urls import path
from . import views

urlpatterns = [
    path('YouTube_API/<str:videoid>/', views.CommentList.as_view()),
    path('YouTube_API/reply/<int:comment_id>/', views.ReplyList.as_view()),
    path('YouTube_API/reply/', views.ReplyList.as_view()),
    path('YouTube_API/<int:pk>/', views.CommentDetail.as_view()),
    path('YouTube_API/', views.CommentList.as_view()),
]
