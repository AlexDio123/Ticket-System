import django_filters
from tickets.models import Ticket

class TicketFilter(django_filters.FilterSet):
    class Meta:
        model= Ticket
        fields = ["start_date", "end_date", 'status']