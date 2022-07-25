from django.urls import path
from blogapp.views import BlogList, BlogDetail

urlpatterns = [
    path('main/', BlogList.as_view()),
    path('main/<int:pk>', BlogDetail.as_view()),
]
