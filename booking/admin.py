from django.contrib import admin

from booking.models import (
    Car,
    CarType,
    Client,
    RentalService,
    BookingRequest,

)
from common.utils import all_fields_names


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    """Админка CarType."""

    list_display = all_fields_names(CarType)



@admin.register(RentalService)
class RentalServiceAdmin(admin.ModelAdmin):
    """Админка RentalService."""

    list_display = all_fields_names(RentalService)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Админка Car."""

    list_display = all_fields_names(Car)
    exclude = ['uuid']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Админка Client."""

    list_display = all_fields_names(Client)


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    """Админка BookingRequest."""

    list_display = all_fields_names(BookingRequest)
