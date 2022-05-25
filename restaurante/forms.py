from django import forms
from .models import ItemMenu, Gallery, Event, Restaurant, Users, Reservation
from django.db.models import fields

class ItemMenuForm(forms.ModelForm):

    class Meta:
        model = ItemMenu
        fields = '__all__'