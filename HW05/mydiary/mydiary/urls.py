"""mydiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from diaryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('daily/', include('daily.urls')),
    path('accounts/', include('accounts.urls')),
    path('new/', views.new, name='new'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'), # model form
    path('formcreate/', views.formcreate, name='formcreate'), # django form
    path('diarylist', views.diarylist, name='diarylist'),
    path('edit/', views.edit, name='edit'),
    path('diaryupdate/<int:diary_id>', views.diaryupdate, name='diaryupdate'),
    path('diarydelete/<int:diary_id>', views.diarydelete, name='diarydelete'),
    path('result',views.result, name='result'),
    path('commentcreate/<int:diary_id>', views.commentcreate, name='commentcreate'),
    path('detail/<int:diary_id>', views.detail, name='detail'),
    path('commentupdate/<int:comment_id>', views.commentupdate, name='commentupdate'),
    path('commentdelete/<int:comment_id>', views.commentdelete, name='commentdelete'),
]
