import django_filters
from tickets.models import Ticket
from django.forms.widgets import DateTimeInput


class TicketFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(widget=DateTimeInput(attrs={'type': 'date'}))
    end_date = django_filters.DateFilter(widget=DateTimeInput(attrs={'type': 'date'}))
    class Meta:
        model= Ticket
        fields = ["start_date", "end_date", 'status']