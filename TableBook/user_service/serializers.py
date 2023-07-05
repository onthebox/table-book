from rest_framework import serializers

from .models import RestaurantChain, RestaurantBranch, BranchAddress

class RestarauntSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantChain
        fields = ('chain_name', 'chain_id')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchAddress
        fields = ('country_name', 'city_name', 'street_name', 'building_name')

class BranchSerializer(serializers.ModelSerializer):
    chain_id = serializers.StringRelatedField()
    address = AddressSerializer()

    def create(self, validated_data):
        
        current_address = validated_data.pop('address')
        address, status = BranchAddress.objects.get_or_create(**current_address)
        branch = RestaurantBranch.objects.create(**validated_data, address = address)
        return branch

    class Meta:
        model = RestaurantBranch
        fields = ('branch_id', 'chain_id', 'contact_number', 'email', 'number_of_tables', 'address')

