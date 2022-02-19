from django.shortcuts import render
#drf
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# models
from ..models import City,DistanceBethwenCities

# serielizers
from ..serializer import CitySerializer, DistanceBethwenCitiesSerializer

#index
def fleet_admin_home(request):
    context = {}
    return render(request, 'fleet_admin/fleet_admin_home.html', context)

class CitiesListAPIView(APIView):
    """
    List all cities, or create a new city.

    POST:
        {
            "name": "ciudad a"
        }
    """
    def get(self, request, format=None):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailAPIView(APIView):
    """
    Retrieve, update or delete a city instance.
    """
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DistanceBethwenCitiesListAPIView(APIView):
    """
    List all doctances, or create a new distance bethwen city.
    """
    def get(self, request, format=None):
        distance = DistanceBethwenCities.objects.all()
        serializer = DistanceBethwenCitiesSerializer(distance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DistanceBethwenCitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistanceBethwenCitiesDetailAPIView(APIView):
    """
    Retrive,update or delete distances bethwen cities
    """
    def get_object(self, pk):
        try:
            return DistanceBethwenCities.objects.get(pk=pk)
        except DistanceBethwenCities.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        distance = self.get_object(pk)
        serializer = DistanceBethwenCitiesSerializer(distance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        distance = self.get_object(pk)
        serializer = DistanceBethwenCitiesSerializer(distance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        distance = self.get_object(pk)
        distance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)