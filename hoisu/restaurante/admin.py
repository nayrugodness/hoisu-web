from django.contrib import admin
from .models import Gallery, Event, Restaurant, Reservation
# Register your models here.


admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(Restaurant)
admin.site.register(Reservation)