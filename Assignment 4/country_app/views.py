from django.shortcuts import render
from rest_framework import generics
from .models import Country
from .serializers import Countrieserializer, Countrieserializer

# Create your views here.
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = Countrieserializer
    
class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = Countrieserializer