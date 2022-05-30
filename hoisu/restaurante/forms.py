from django import forms
from .models import ItemMenu, Gallery, Event, Restaurant, Users, Reservation
from django.db.models import fields

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

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)