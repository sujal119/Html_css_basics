from django.shortcuts import render
from rest_framework import generics

from animal_app.models import Animal
from .models import Vehicle
from .serializers import  VehicleSerializer

# Create your views here.
class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer