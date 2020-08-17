from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Customer, Destination, Item
import os
from pathlib import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def datatables(request):
    customers = Customer.objects.all()
    return render(request, "datatables.html", {'customers': customers})


def add_customer(request):
    if request.method == "POST":
        customer = request.POST['customer']
        address = request.POST['address']
        mobile = request.POST['mobile']
        city = request.POST['city']
        state = request.POST['state']
        gst = request.POST['gst']
        data = Customer.objects.create(name=customer, address=address, mobile_no=mobile, city=city, state=state,
                                       gst_no=gst)
        data.save()
        return redirect('datatables')

    else:
        return redirect('datatables')


def add_invoice(request):
    if request.method == "POST":
        customer = request.POST['customer_id']
        title = request.POST['title']
        invoice_no = request.POST['invoice_num']
        city = request.POST['city']
        state = request.POST['state']
        gst = request.POST['gst']
        data = Customer.objects.create(name=customer, address=address, mobile_no=mobile, city=city, state=state,
                                       gst_no=gst)
        data.save()
        return redirect('bill')

    else:
        return redirect('bill')


def remove_customer(request):
    if request.method == "POST":
        customer_id = request.POST['id']
        Customer.objects.get(pk=customer_id).delete()
        return redirect('datatables')
    else:
        return redirect('datatables')


def edit_customer(request):
    if request.method == "POST":
        customer_id = request.POST['id']
        customer = Customer.objects.get(pk=customer_id)
        customer.name = request.POST['customer']
        customer.address = request.POST['address']
        customer.mobile_no = request.POST['mobile']
        customer.city = request.POST['city']
        customer.state = request.POST['state']
        customer.gst_no = request.POST['gst']
        customer.save()
        return redirect('datatables')
    else:
        return redirect('datatables')


def bill(request):
    customer = Customer.objects.all()
    return render(request, 'bill.html', {'customer': customer})


def drive(request):
    drive_path = Path('media\\drive')
    return render(request, 'drive.html', {'drive': drive_path.iterdir(), 'path': drive_path})


def drive_path(request, path):
    dir_path = Path(path)
    return render(request, 'drive.html', {'drive': dir_path.iterdir(), 'path': dir_path})


def add_folder(request, path):
    try:
        folder_name = request.POST['folder-name']
        drive_path = Path(f'{path}\\{folder_name}')
        drive_path.mkdir()
    except FileExistsError:
        pass
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def add_file(request, path):
    file_name = request.POST['file-name']
    with open(f'{path}\\' + file_name, 'w') as file:
        pass
    return HttpResponseRedirect(reverse('drive_path', args=[path]))
