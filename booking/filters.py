from django_filters import rest_framework as filters

from booking.models import Car


class CarFilter(filters.FilterSet):
    daily_cost = filters.NumberFilter(field_name='daily_cost', lookup_expr='lte')

    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'car_type',
            'rental_service',
        ]
