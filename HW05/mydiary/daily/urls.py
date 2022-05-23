from django.urls import path
from daily import views

urlpatterns = [
    path('', views.dailydiary, name='dailydiary'),
    path('showdiary/', views.showdiary, name='showdiary'),
]
