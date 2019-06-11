from .serializers import *
from .models import *
from rest_framework import viewsets


class BusLineViewSet(viewsets.ModelViewSet):
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    pagination_class = None
