from django.db import models

# Create your models here.
STATUS_OPTIONS =(
    ('OP', 'OPEN'),
    ('CL', 'CLOSED')
)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    
