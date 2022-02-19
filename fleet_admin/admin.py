from django.contrib import admin

# Register your models here.
from .models import City,Vehicle,DistanceBethwenCities

admin.site.register(City)
admin.site.register(Vehicle)
admin.site.register(DistanceBethwenCities)
