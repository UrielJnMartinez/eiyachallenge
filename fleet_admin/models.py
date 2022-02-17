from django.db import models

# Create your models here.


class City(models.Model):
    name  = models.CharField(verbose_name='ciudad', max_length=50)
    
    class Meta:
        db_table ='city'


class Vehicle(models.Model):
    fuel_usage_km = models.CharField(verbose_name='consumo de combustible', max_length=50)
    spent_fuel = models.CharField(verbose_name='combustible consumido ', max_length=50) 
    distance_covered = models.CharField(verbose_name='Distancia recorrida', max_length=50)
    current_location = models.ForeignKey(
        City, 
        related_name='current_location', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table ='vehicle'


class DistanceBethwenCities(models.Model):
    city_origin = models.ForeignKey(
        City, 
        related_name ='city_origin', 
        on_delete=models.CASCADE
    ) 
    city_arrival = models.ForeignKey(
        City, 
        related_name ='city_arrival', 
        on_delete=models.CASCADE
    ) 
    distance = models.CharField(verbose_name='Distancia', max_length=50)

    class Meta:
        db_table ='dictance_city'