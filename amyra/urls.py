from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("datatables/", views.datatables, name="datatables"),
    path('datatables/add_customer/', views.add_customer, name="add_customer"),
    path('datatables/remove_customer/', views.remove_customer, name="remove_customer"),
    path('datatables/edit_customer/', views.edit_customer, name="edit_customer"),
    path('bill/', views.bill, name="bill"),
    path('bill/add_invoice', views.add_invoice, name="add_invoice"),
    path('drive/', views.drive, name="drive"),
    path('drive/<str:path>/', views.drive_path, name="drive_path"),
    path('add_folder/<str:path>/', views.add_folder, name='add_folder'),
    path('add_file/<str:path>/', views.add_file, name='add_file'),
    path('remove_folder/<str:path>/', views.remove_folder, name='remove_folder'),
    path('rename_folder/<str:path>/', views.rename_folder, name='rename_folder')
]
