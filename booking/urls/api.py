from django.urls import path

from booking.viewsets import ClientDetailView, ClientListView

urlpatterns = [
    path('all-profiles/', ClientListView.as_view(), name='all-profiles'),
    path('profile/<int:pk>/', ClientDetailView.as_view(), name='profile'),
]
