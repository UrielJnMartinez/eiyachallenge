from dataclasses import field
from rest_framework import serializers

# models
from .models import City,Vehicle,DistanceBethwenCities

class cityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['id','name']
class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    fuel_usage_km = serializers.CharField()
    spent_fuel = serializers.CharField()
    distance_covered = serializers.CharField()
    current_location = cityItemSerializer(required=True)
    # current_location = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Vehicle
        fields = ['id','fuel_usage_km','spent_fuel','distance_covered','current_location']
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Vehicle` instance, given the validated data.
        """
        # city = City.objects.filter(pk=validated_data.get('current_location' ))
        new_location = validated_data.pop('current_location')
        current_location = City.objects.filter(pk=new_location)
        vehicle = Vehicle.objects.create(current_location=current_location,**validated_data)
        return vehicle

    def update(self,instance,validated_data):
        """
        Update and return an existing `Vehicle` instance, given the validated data.
        """
        new_location = validated_data.pop('current_location')
        current_location = City.objects.filter(pk=new_location)

        instance.fuel_usage_km = validated_data.get('fuel_usage_km', instance.fuel_usage_km)
        instance.spent_fuel = validated_data.get('spent_fuel', instance.spent_fuel)
        instance.distance_covered = validated_data.get('distance_covered', instance.distance_covered)
        instance.current_location = current_location
        
        instance.save()
        return instance

class CitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    vehicle = VehicleSerializer(source='current_location',many=True)
    class Meta:
        model = City
        fields = ['id','name','vehicle']
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `City` instance, given the validated data.
        """
        return City.objects.create(**validated_data)

    def update(self,instance,validated_data):
        """
        
        Update and return an existing `City` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        
        instance.save()
        return instance



class DistanceBethwenCitiesSerializer(serializers.ModelSerializer):
    city_origin = cityItemSerializer(required=True)
    city_arrival = cityItemSerializer(required=True)
    distance = serializers.CharField()

    class Meta:
        model = DistanceBethwenCities
        fields = ['id','city_origin','city_arrival','distance']


    def create(self, validated_data):
        """
        Create and return a new distance bethwen city instance, given the validated data.
        """
        return DistanceBethwenCities.objects.create(**validated_data)

    def update(self,instance,validated_data):
        """
        Update and return an existing distance bethwen city instance, given the validated data.
        """
        instance.city_origin = validated_data.get('city_origin', instance.city_origin)
        instance.city_arrival = validated_data.get('city_arrival', instance.city_arrival)
        instance.distance = validated_data.get('distance', instance.distance)
        
        instance.save()
        return instance