from django.shortcuts import render
from rest_framework import generics

from .models import RestaurantChain
from .serializers import RestarauntSerializer

class ChainList(generics.ListCreateAPIView):
    queryset = RestaurantChain.objects.all()
    serializer_class = RestarauntSerializer


class ChainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantChain.objects.all()
    serializer_class = RestarauntSerializer
