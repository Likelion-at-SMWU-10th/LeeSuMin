from django.urls import path
from daily import views

urlpatterns = [
    path('', views.dailydiary),
    path('showdiary/', views.showdiary),
]
