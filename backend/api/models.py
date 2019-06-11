from django.db import models
from django.contrib.auth.models import User


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
