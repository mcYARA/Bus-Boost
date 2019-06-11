from .models import *
from rest_framework import serializers


class BusLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLine
        fields = (
            'pk', 'depart_settlement', 'arrive_settlement', 'depart_time', 'arrive_time', 'price', 'count_of_seats',
        )
