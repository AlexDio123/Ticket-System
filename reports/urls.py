from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.reports_list, name="reports_filter"),
]
