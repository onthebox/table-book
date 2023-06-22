from rest_framework import serializers

from .models import RestaurantChain

class RestarauntSerializer(serializers.Serializer):
    class Meta:
        model = RestaurantChain
        fields = ('name', 'id')

