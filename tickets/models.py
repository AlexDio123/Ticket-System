from django.db import models
from employee.models import Employee
import datetime


# Create your models here.
STATUS_OPTIONS = (
    ("OP", "OPEN"),
    ("CL", "CLOSED")
)

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description= models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    notes = models.TextField(null=True)

    
    def __str__(self):
        return self.subject
    
