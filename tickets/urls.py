from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="ticket_list"),
    path('create_ticket/', views.create_ticket, name="ticket_create"),
    path('update_ticket/<str:pk>/', views.update_ticket, name="ticket_update"),
    path('delete_ticket/<str:pk>/', views.delete_ticket, name="ticket_delete"),
]
