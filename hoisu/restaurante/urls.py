from django.urls import path, include
from . import views
from . import models
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.create_restaurant, name='registrar'),
    path('modificar-restaurante/<slug:slug>', views.update_restaurant, name='modificar-restaurante'),
    path('modificar-reservacion/<slug:slug>', views.update_reservation, name='modificar-reservación'),
    path('reservar/', views.create_reservation, name='reservar'),
    path('listar/', views.list_restaurants, name='listar'),
]