from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Restaurant, Users, Reservation, Ciudad, Categoria
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

    price_min = forms.CharField(
        max_length=100,
        required=True,
        help_text='Precio mínimo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 10,000'}),
    )

    price_max = forms.CharField(
        max_length=100,
        required=True,
        help_text='Precio máximo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 60,000'}),
    )
    city = forms.ChoiceField(help_text='Ciudad', choices=Ciudad)
    type = forms.ChoiceField(help_text='Categoría', choices=Categoria)
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Correo electrónico',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'restaurante@gmail.com'}),
    )
    description = forms.CharField(
        max_length=1000,
        required=True,
        help_text='Descripción del restaurante',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lorem ipsum dolor sept...'}),
    )
    place = forms.CharField(
        max_length=10,
        required=True,
        help_text='Dirección ',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Ejemplo: Km 7 vía Caimo'}),
    )
    parking = forms.BooleanField(
        help_text='¿Tiene parqueadero?',
        widget=forms.CheckboxInput(attrs={"class": "checkbox"})
    )
    credit_card = forms.BooleanField(
        help_text='¿Acepta tarjeta de crédito?',
        widget=forms.CheckboxInput(attrs={"class": "checkbox"})
    )
    debit_card = forms.BooleanField(
        help_text='¿Acepta tarjeta débito?',
        widget=forms.CheckboxInput(attrs={"class": "checkbox"})
    )

    class Meta:
        model = Restaurant
        fields = [
            'name', 'cell', 'city', 'price_min', 'price_max', 'menu', 'email', 'description', 'type',
            'place', 'principal_image', 'credit_card', 'debit_card'
        ]


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Nombres',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    lastname = forms.CharField(
        max_length=100,
        required=True,
        help_text='Apellidos',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        required=True,
        help_text='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: nombre@gmail.com'}),
    )
    cell = forms.CharField(
        max_length=100,
        required=True,
        help_text='Número telefónico',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 3156277777'}),
    )
    customers = forms.CharField(
        max_length=100,
        required=True,
        help_text='Número de personas',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 2 '}),
    )

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


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']