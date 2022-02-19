
from django.urls import path
from .views import cities,vehicles


urlpatterns = [
    path('', cities.fleet_admin_home, name='fleet_admin_home'),
    #vehicles
    path('vehicles/', vehicles.VehiclesListAPIView.as_view(), name='vehicles_list'),
    path('vehicles/detail/<int:pk>/', vehicles.VehicleDetailAPIView.as_view(), name='vehicle_detail'),
    # city
    path('cities/', cities.CitiesListAPIView.as_view(), name='cities_list'),
    path('cities/detail/<int:pk>/', cities.CityDetailAPIView.as_view(), name='city_detail'),
    # distances
    path('distances/', cities.DistanceBethwenCitiesListAPIView.as_view(), name='distances_list'),
    path('distances/detail/<int:pk>/', cities.DistanceBethwenCitiesDetailAPIView.as_view(), name='distances_detail'),
]