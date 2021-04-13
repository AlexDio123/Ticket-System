from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="ticket_list"),
    path('login/', views.login_page, name="login"),
    path('logout',views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('create_ticket/', views.create_ticket, name="ticket_create"),
    path('update_ticket/<str:pk>/', views.update_ticket, name="ticket_update"),
    path('delete_ticket/<str:pk>/', views.delete_ticket, name="ticket_delete"),
    path('info_ticket/<str:pk>/', views.info_ticket, name="info_ticket"),

]
