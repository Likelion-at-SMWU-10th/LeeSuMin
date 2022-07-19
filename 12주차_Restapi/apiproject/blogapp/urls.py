from django.urls import path
from blogapp.views import BlogList, BlogDetail

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),
]
