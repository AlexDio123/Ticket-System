from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def create_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request, 'employee/add_form.html', context)
