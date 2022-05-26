from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import ItemMenu, Gallery, Event, Restaurant, Reservation
from .forms import ItemMenuForm, GalleryForm, EventForm, RestaurantForm, ReservationForm
from rest_framework import viewsets
from .serializers import ItemMenuSerializer, GallerySerializer, EventSerializer, RestaurantSerializer, ReservationSerializer
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView

def list_restaurants(request):
    restaurant = Restaurant.objects.all()

    data = {
        'restaurant': restaurant
    }

    return render(request, 'app/restaurant/list.html', data)

def create_restaurant(request):
    data = {
        'form': RestaurantForm()
    }

    if request.method == 'POST':
        formulario = RestaurantForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return render(request, 'app/restaurant/create.html', data)

def update_restaurant(request, slug):

    restaurant = get_object_or_404(Restaurant, slug=slug)

    data = {
        'form' : RestaurantForm(instance=restaurant)
    }

    if request.method == 'POST':

        formulario = RestaurantForm(data=request.POST, instance=restaurant, files=request.FILES)

        if formulario.is_valid():

            formulario.save()

        data["form"] = formulario

    return render(request, 'app/restaurant/update.html', data)

def create_reservation(request):
    data = {
        'form': ReservationForm()
    }

    if request.method == 'POST':
        formulario = ReservationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return render(request, 'app/reservation/create.html', data)

def update_reservation(request, slug):

    reservation = get_object_or_404(Reservation, slug=slug)

    data = {
        'form' : ReservationForm(instance=reservation)
    }

    if request.method == 'POST':

        formulario = RestaurantForm(data=request.POST, instance=reservation, files=request.FILES)

        if formulario.is_valid():

            formulario.save()

        data["form"] = formulario

    return render(request, 'app/reservation/update.html', data)