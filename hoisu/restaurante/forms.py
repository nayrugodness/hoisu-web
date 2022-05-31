from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Restaurant, Users, Reservation
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))


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

    departamento = forms.CharField(
        max_length=100,
        required=True,
        help_text='Departamento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Departamento'}),
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
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Km 7 vía Caimo'}),
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