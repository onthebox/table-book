from django.shortcuts import render
from rest_framework import viewsets

from .models import RestaurantChain, RestaurantBranch
from .serializers import RestarauntSerializer, BranchSerializer

class ChainViewSet(viewsets.ModelViewSet):
    queryset = RestaurantChain.objects.all()
    serializer_class = RestarauntSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = RestaurantBranch.objects.all()
    serializer_class = BranchSerializer
