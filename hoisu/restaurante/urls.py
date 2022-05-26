from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.ReservationFormView.as_view(), name='reservar'),
    path('success', views.success, name='success'),
]