# from django.shortcuts import render
# from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RestaurantChain
from .serializers import RestaurantChainSerializer


class ChainsView(APIView):

    def get(self, request):
        """
        Get all data from RestaurantChain model.
        """
        chains = RestaurantChain.objects.all()
        chains_serialized = RestaurantChainSerializer(chains, many=True)

        return Response(chains_serialized.data)
