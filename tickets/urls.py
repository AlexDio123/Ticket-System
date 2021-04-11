from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.create_ticket, name="ticket_create"),
]
