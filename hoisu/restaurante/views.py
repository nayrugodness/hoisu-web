from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import ItemMenu, Gallery, Event, Restaurant, Reservation
from .forms import  ItemMenuForm, GalleryForm, EventForm, RestaurantForm, ReservationForm
from rest_framework import viewsets