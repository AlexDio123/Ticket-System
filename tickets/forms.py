from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import DateTimeInput
from django.contrib.auth.models import User
from .models import Ticket
from employee.models import Employee



class TicketForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateTimeInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=DateTimeInput(attrs={'type': 'date'}))
    class Meta:
        model = Ticket
        fields = ['subject','employee','description','status','start_date','end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("La fecha final debe ser mayor que la fecha inicial.")


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    

