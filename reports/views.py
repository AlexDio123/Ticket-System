from django.shortcuts import render
from .filters import TicketFilter
from tickets.models import Ticket
# Create your views here.

def reports_list(request):
    ticket_report = Ticket.objects.all()
    reports_form = TicketFilter(request.GET, queryset=ticket_report)
    ticket_report = reports_form.qs
    context={'ticket_report':ticket_report, 'reports_form':reports_form}
    return render(request, 'reports/reports_list.html', context)
