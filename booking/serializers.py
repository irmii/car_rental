from rest_framework import serializers
from booking.models import (
    Client,
    CarType,
    RentalService,
Car,
)


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = '__all__'


class RentalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalService
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
