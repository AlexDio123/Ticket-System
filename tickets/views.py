from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import TicketForm, CreateUserForm
from .models import Ticket
# Create your views here.

#Login page
def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('ticket_list')
    context={}
    return render(request, 'tickets/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

#Register Page
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'tickets/register.html', context)

# Home page
def index(request):
    tickets = Ticket.objects.all()
    context={"tickets":tickets}
    return render(request, 'tickets/tickets_list.html', context)

# Create Ticket page
def create_ticket(request):
    form = TicketForm()

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form":form,}
    return render(request, "tickets/tickets_add.html", context)

# Update Ticket page
def update_ticket(request, pk):

    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    
    context = {"form":form,"notes":notes}
    return render(request, "tickets/tickets_add.html", context)

# Update Ticket Page
def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect('/')
    context ={'ticket':ticket}
    return render(request, 'tickets/tickets_delete.html', context)

# Details Page for tickets
def info_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    context={"ticket":ticket}
    return render(request, 'tickets/tickets_info.html', context)
