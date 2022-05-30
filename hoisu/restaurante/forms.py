from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import ItemMenu, Gallery, Event, Restaurant, Users, Reservation
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemMenuForm(forms.ModelForm):

    class Meta:
        model = ItemMenu
        fields = '__all__'

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

class RestaurantForm(forms.ModelForm):

    parking = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"checkbox"}))
    credit_card = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "checkbox"}))
    debit_card = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "checkbox"}))
    class Meta:
        model = Restaurant
        fields = '__all__'



class ReservationForm(forms.ModelForm):


    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'reservation': forms.SelectDateWidget()
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    check = forms.BooleanField(required=True)