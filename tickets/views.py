from django.shortcuts import render
from .forms import TicketForm
# Create your views here.

def create_ticket(request):
    form = TicketForm()

    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form":form,}
    return render(request, "tickets/tickets_add.html", context)
