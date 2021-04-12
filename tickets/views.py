from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
# Create your views here.


def index(request):
    tickets = Ticket.objects.all()
    context={"tickets":tickets}
    return render(request, 'tickets/tickets_list.html', context)


def create_ticket(request):
    form = TicketForm()

    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tickets/')

    context = {"form":form,}
    return render(request, "tickets/tickets_add.html", context)

def update_ticket(request, pk):

    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/tickets/')

    context = {"form":form,}
    return render(request, "tickets/tickets_add.html", context)

def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect('/tickets/')
    context ={'ticket':ticket}
    return render(request, 'tickets/tickets_delete.html', context)

