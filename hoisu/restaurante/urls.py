from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('registrar-restaurante/', views.restaurant_create(), name='registrar-restaurante'),
]