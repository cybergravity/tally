from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("datatables/", views.datatables, name="datatables"),
    path('datatables/add_customer/', views.add_customer, name="add_customer"),
    path('datatables/remove_customer/', views.add_customer, name="remove_customer")
]