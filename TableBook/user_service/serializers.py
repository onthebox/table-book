from rest_framework import serializers

from .models import RestaurantBranch, RestaurantChain


class RestaurantBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantBranch
        fields = '__all__'


class RestaurantChainSerializer(serializers.ModelSerializer):

    branches = RestaurantBranchSerializer(many=True)

    class Meta:
        model = RestaurantChain
        fields = ['chain_name', 'branches']
