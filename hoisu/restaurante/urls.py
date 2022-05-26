from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('registrar-restaurante/', views.RestaurantCreateView.as_view(), name='registrar-restaurante'),
    path('reservar', views.ReservationCreateView.as_view(), name='reservar'),
    path('modificar-restaurante', views.RestaurantUpdateView.as_view(), name='modificar-restaurante'),
    path('success', views.success, name='success'),
]