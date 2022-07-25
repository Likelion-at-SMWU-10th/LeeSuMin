from django.urls import path
from commentapp.views import CommentList, CommentDetail, BlogCommentList

urlpatterns = [
    path('main/', CommentList.as_view()),
    path('blog/<int:pk>', BlogCommentList.as_view()),
    path('main/<int:pk>', CommentDetail.as_view()),
]
