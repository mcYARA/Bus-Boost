from .serializers import *
from .models import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class BusLineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    pagination_class = None

    @action(detail=True, methods=['get'])
    def book_ticket(self, request, pk):
        bus_line = self.get_object()
        bus_line.book_ticket(request.user)
        return Response(status=status.HTTP_202_ACCEPTED)
