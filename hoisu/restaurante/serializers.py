from django.db.models.query import QuerySet
from .models import  Restaurant, Reservation
from rest_framework import fields, serializers



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'