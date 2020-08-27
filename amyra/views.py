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


def drive(request):
    drive_path = Path('media'+ os.path.sep + 'drive')
    return render(request, 'drive.html', {'drive': drive_path.iterdir(), 'path': drive_path, 'showBack': False})


def drive_path(request, path):
    dir_path = Path(path)
    showBack = True
    index = path.rfind("\\")
    if path == 'media\\drive':
        showBack = False
    return render(request, 'drive.html', {'drive': dir_path.iterdir(), 'path': dir_path, 'back': path[:index], 'showBack': showBack})


def add_folder(request, path):
    try:
        folder_name = request.POST['folder-name']
        drive_path = Path(f'{path}' + os.path.sep + f'{folder_name}')
        drive_path.mkdir()
    except FileExistsError:
        pass
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def add_file(request, path):
    file_name = request.POST['file-name']
    if file_name.count(".") < 1:
        messages.success(request, "File Must have extension")
    else:
        with open(path + os.path.sep + file_name, 'w') as file:
            pass
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def remove_folder(request, path):
    folder_poth = request.POST['folder-path']
    folder_to_remove = Path(folder_poth)
    shutil.rmtree(folder_to_remove)
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def rename_folder(request, path):
    name = request.POST['folder-name']
    folder_poth = request.POST['folder-path']
    folder_to_rename = Path(folder_poth)
    try:
        folder_to_rename.rename(path + os.path.sep + name)
    except FileExistsError:
        messages.success(request, "Folder already exist. Please choose other name to continue")
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def remove_file(request, path):
    file = request.POST['file-path']
    os.remove(file)
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


def rename_file(request, path):
    file = request.POST['file-path']
    name = request.POST['file-name']
    if name.count(".") < 1:
        messages.success(request, "File Must have extension")
    else:
        os.rename(file, path + os.path.sep + name)
    return HttpResponseRedirect(reverse('drive_path', args=[path]))


class BasicUploadView(View):
    def get(self, request):
        file_lists = Files.objects.all()
        return render(self.request, 'index.html', {'files': file_lists})

    def post(self, request):
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save()
            data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ImageUploadView(View):
    def get(self, request):
        image_lists = Images.objects.all()
        return render(self.request, 'index.html', {'files': image_lists})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class PDFUploadView(View):
    def get(self, request):
        pdf_lists = PDFForm.objects.all()
        return render(self.request, 'index.html', {'files': pdf_lists})

    def post(self, request):
        form = PDFForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            pdf = form.save()
            data = {'is_valid': True, 'name': pdf.file.name, 'url': pdf.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
