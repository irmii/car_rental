from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth-authtoken/', include('djoser.urls.authtoken')),
    path('api/', include('booking.urls.api')),
]
