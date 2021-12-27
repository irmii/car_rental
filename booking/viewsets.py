from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from booking.models import Client
from booking.permissions import IsOwnerProfileOrReadOnly
from booking.serializers import ClientSerializer


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
