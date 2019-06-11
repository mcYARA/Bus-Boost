from django.contrib import admin
from .models import *


@admin.register(BusLine)
class BusLineAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'depart_settlement', 'depart_time', 'arrive_settlement', 'arrive_time', 'count_of_seats', 'price',
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'seat_number', 'bus_line',)
