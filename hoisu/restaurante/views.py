from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import ItemMenu, Gallery, Event, Restaurant, Reservation
from .forms import  ItemMenuForm, GalleryForm, EventForm, RestaurantForm, ReservationForm
from rest_framework import viewsets
from .serializers import ItemMenuSerializer, GallerySerializer, EventSerializer, RestaurantSerializer, ReservationSerializer
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormView

