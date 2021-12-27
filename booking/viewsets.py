from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from booking.models import (
    Client,
    CarType,
    RentalService,
    Car,
)
from booking.permissions import IsOwnerProfileOrReadOnly
from booking.serializers import (
    ClientSerializer,
    CarTypeSerializer,
    RentalServiceSerializer,
    CarSerializer,
)
from booking.filters import CarFilter


class ClientListView(ListAPIView):
    """Метод для получения списка клиентов, доступен только сотруднику is_staff = True."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]


class ClientDetailView(RetrieveUpdateDestroyAPIView):
    """Метод для изменения профиля пользователя, доступен только владельцу профиля."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class CarTypeListView(ListAPIView):
    """Метод для получения списка типов машин."""
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
    permission_classes = [IsAuthenticated]


class RentalServiceListView(ListAPIView):
    """Метод для получения списка прокатных сервисов."""
    queryset = RentalService.objects.all()
    serializer_class = RentalServiceSerializer
    permission_classes = [IsAuthenticated]


class CarListView(ListAPIView):
    """Метод для получения списка машин."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
