from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from . import models
from rest_framework import routers

from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.create_restaurant, name='registrar'),
    path('modificar-restaurante/<slug:slug>', views.update_restaurant, name='modificar-restaurante'),
    path('restaurante/<slug:slug>', views.RestaurantDetailView.as_view(), name='detalle'),
    path('modificar-reservacion/<slug:slug>', views.update_reservation, name='modificar-reservación'),
    path('reservar/<slug:slug>', views.create_reservation, name='reservar'),
    path('listar/', views.list_restaurants, name='listar'),
    path('listar-reservaciones/<id>', views.list_reservations, name='reservaciones'),
]