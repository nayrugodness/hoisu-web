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
    name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Nombre del restaurante',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del restaurante'}),
    )
    cell = forms.CharField(
        max_length=100,
        required=True,
        help_text='Número telefónico',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número telefónico'}),
    )
    city = forms.ChoiceField(

        required=True,
        help_text='Ciudad',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
    )
    departamento = forms.CharField(
        max_length=100,
        required=True,
        help_text='Departamento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Departamento'}),
    )
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
        help_text='Ingresa tu correo electrónico',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Escribe tu nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Escribe tus apellidos',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Escribe tu nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
    )
    password1 = forms.CharField(
        help_text='Ingresa tu contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Confirma tu contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
    )
    check = forms.BooleanField(required=True)

    class Meta:
        model = User

        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
        ]