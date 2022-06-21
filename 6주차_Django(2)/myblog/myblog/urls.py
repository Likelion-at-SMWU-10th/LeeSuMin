from django.contrib import admin
from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('developer/', include('developer.urls')),
    path('accounts/', include('accounts.urls')),
]
