from django.contrib.auth.models import User
from django.db import models
import uuid

from phonenumber_field.modelfields import PhoneNumberField
from common.const import MAXLENGTH15, MAXLENGTH50, MAXLENGTH200


class RentalService(models.Model):
    """Модель проката."""

    name = models.CharField(
        'Название прокатного сервиса',
        max_length=MAXLENGTH50,
    )
    address = models.CharField(
        'Адрес прокатного сервиса',
        max_length=MAXLENGTH200,
    )

    class Meta(object):
        verbose_name = 'Прокат'
        verbose_name_plural = 'Прокаты'

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: type
        """
        return self.name


class CarType(models.Model):
    """Тип автомобиля."""

    type = models.CharField(
        'Тип автомобиля: легковой, грузовой, лимузин',
        max_length=MAXLENGTH50,
    )

    class Meta(object):
        verbose_name = 'Тип автомобиля'
        verbose_name_plural = 'Тип автомобиля'

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: name
        """
        return self.type


class Car(models.Model):
    """Модель автомобиля"""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(
        'Марка автомобиля',
        max_length=MAXLENGTH50,
    )
    model = models.CharField(
        'Модель автомобиля',
        max_length=MAXLENGTH50,
    )
    license_plate = models.CharField(
        'Государственный номер',
        max_length=MAXLENGTH50,
    )
    car_type = models.ForeignKey(
        CarType,
        related_name='car_types',
        on_delete=models.CASCADE,
    )
    daily_cost = models.FloatField(
        'Посуточная стоимость аренды, в рублях',
    )
    rental_service = models.ForeignKey(
        RentalService,
        related_name='car_rental_services',
        on_delete=models.CASCADE,
    )

    class Meta(object):
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: name
        """
        return self.license_plate


class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    first_name = models.TextField(max_length=MAXLENGTH200, null=True)
    second_name = models.TextField(max_length=MAXLENGTH200, null=True)
    third_name = models.TextField(max_length=MAXLENGTH200, null=True)
    address = models.CharField(max_length=MAXLENGTH200, null=True)
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length=MAXLENGTH200, null=True)
    experience = models.IntegerField(
        'Стаж, в целых годах',
        null=True,
    )
    drivers_license = models.IntegerField(
        'Номер водительского удостоверения',
        null=True,
    )

    class Meta(object):
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: username
        """
        return self.user.username


class BookingRequest(models.Model):
    """Модель заявки на бронирование."""

    STATUSES = (
        ('created', 'Создана'),
        ('in_progress', 'На рассмотрении'),
        ('approved', 'Бронирование подтверждено'),
        ('canceled', 'Отменено'),
    )

    client = models.ForeignKey(
        Client,
        related_name='client_booking_request',
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        related_name='car_booking_request',
        on_delete=models.CASCADE,
    )
    start_of_booking = models.DateField('Дата начала бронирования')
    end_of_booking = models.DateField('Дата окончания бронирования')
    request_status = models.CharField(
        'Статус заявки на бронирование',
        choices=STATUSES,
        max_length=MAXLENGTH15,
    )

    class Meta(object):
        verbose_name = 'Заявка на бронирование'
        verbose_name_plural = 'Заявки на бронирование'

    def __str__(self):
        """Строковое представление объекта.

        Returns:
            str: car + client
        """
        return self.car.license_plate + ' ' + self.client.user.username
