from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.create_employee, name="employee_create"),
]
