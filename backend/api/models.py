from django.db import models
from django.contrib.auth.models import User


class SeatsDoesntAvailable(Exception):
    pass


class BusLine(models.Model):
    class Meta:
        verbose_name = 'рейс'
        verbose_name_plural = 'рейси'

    depart_settlement = models.CharField('Пункт відправлення', max_length=100)
    arrive_settlement = models.CharField('Пункт прибуття', max_length=100)

    depart_time = models.DateTimeField('Час відправлення')
    arrive_time = models.DateTimeField('Час прибуття')

    price = models.FloatField('Ціна')

    count_of_seats = models.SmallIntegerField('Кільсть сидінь')

    def has_available_seats(self):
        """
        Перевіряє чи є доступні місця
        :return: True, або False
        """
        if self.ticket_set.count() < self.count_of_seats:
            return True
        return False

    def book_ticket(self, user):
        if not self.has_available_seats():
            raise SeatsDoesntAvailable
        Ticket.objects.create(
            user=user,
            seat_number=self.ticket_set.count() + 1,
            bus_line=self,
        )

    def __str__(self):
        return f'{self.depart_settlement} - {self.arrive_settlement}'


class Ticket(models.Model):
    class Meta:
        verbose_name = 'квиток'
        verbose_name_plural = 'квитки'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.SmallIntegerField('Номер сидіння')
    bus_line = models.ForeignKey(BusLine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} ({self.bus_line})'
