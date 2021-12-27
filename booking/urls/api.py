from django.urls import path

from booking.viewsets import (
    ClientDetailView,
    ClientListView,
    CarTypeListView,
    RentalServiceListView,
    CarListView,
)

urlpatterns = [
    path('all-profiles/', ClientListView.as_view(), name='all-profiles'),
    path('profile/<int:pk>/', ClientDetailView.as_view(), name='profile'),
    path('car_types/', CarTypeListView.as_view(), name='car_types'),
    path('rental_service/', RentalServiceListView.as_view(), name='rental_service'),
    path('cars/', CarListView.as_view(), name='cars'),
]
