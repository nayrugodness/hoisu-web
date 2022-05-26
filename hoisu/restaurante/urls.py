from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('registrar-restaurante/', views.RestaurantCreateView.as_view(), name='registrar-restaurante'),
    path('success', views.success, name='success'),
]