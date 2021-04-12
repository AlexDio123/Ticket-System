from django.shortcuts import render, redirect
from .forms import EmployeeForm

# Create your views here.

def create_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/tickets/')
    context = {"form":form}
    return render(request, 'employee/add_form.html', context)
