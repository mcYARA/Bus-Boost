from .models import *
from rest_framework import serializers


class BusLineSerializer(serializers.ModelSerializer):
    depart_time_str = serializers.SerializerMethodField('depart_time')

    def depart_time(self, obj):
        return obj.depart_time.strftime("%m-%d %H:%M:%S")

    arrive_time_str = serializers.SerializerMethodField('arrive_time')

    def arrive_time(self, obj):
        return obj.arrive_time.strftime("%m-%d %H:%M:%S")

    class Meta:
        model = BusLine
        fields = (
            'pk', 'depart_settlement', 'arrive_settlement', 'depart_time_str', 'arrive_time_str', 'price',
            'count_of_seats',
        )
