from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('registrar/', views.create_restaurant, name='registrar'),
    path('reservar/', views.create_reservation, name='reservar'),
    path('listar/', views.list_restaurants, name='listar'),
]