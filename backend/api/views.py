from .serializers import *
from .models import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import *
from rest_framework.permissions import IsAuthenticated


class BusLineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    pagination_class = None

    @action(detail=True, methods=['get'])
    def book_ticket(self, request, pk):
        bus_line = self.get_object()
        bus_line.book_ticket(request.user)
        return Response(status=status.HTTP_202_ACCEPTED)


class TicketViewSet(viewsets.ModelViewSet):
    permissions = (IsAuthenticated, OwnProfilePermission,)
    serializer_class = TicketSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return Ticket.objects.all().filter(user=self.request.user)
