from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import View
from .models import Customer, Destination, Item, Images
import os
from pathlib import *
import shutil
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm, FileForm, PDFForm
from .models import Files
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
