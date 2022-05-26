from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import ItemMenu, Gallery, Event, Restaurant, Reservation
from .forms import ItemMenuForm, GalleryForm, EventForm, RestaurantForm, ReservationForm
from rest_framework import viewsets
from .serializers import ItemMenuSerializer, GallerySerializer, EventSerializer, RestaurantSerializer, ReservationSerializer
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView

class RestaurantFormView(FormView):
    template_name = 'app/restaurant/create.html'
    form_class = RestaurantForm
    success_url = 'success'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

def success(request):


    return render(request, 'app/restaurant/success.html')