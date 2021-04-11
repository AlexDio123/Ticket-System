from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject','employee','description','status']

class TicketTimeEntryForm(forms.ModelForm):
    class Meta:
        model= Ticket
        fields = ['start_date','end_date','notes']


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
    

