from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def create_employee(request):
    form = EmployeeForm()
    context = {"form":form}
    return render(request, 'employee/add_form.html', context)
