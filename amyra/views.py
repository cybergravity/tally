from django.shortcuts import render , redirect
from .models import Customer
# Create your views here.


def index(request):
    return render(request, "index.html")

def datatables(request):
    customers = Customer.objects.all()
    return render(request,"datatables.html", {'customers': customers})


def add_customer(request):
    if request.method == "POST":
        customer = request.POST['customer']
        address = request.POST['address']
        mobile = request.POST['mobile']
        city = request.POST['city']
        state = request.POST['state']
        gst = request.POST['gst']
        data = Customer.objects.create(name = customer, address = address, mobile_no = mobile, city = city, state=state, gst_no = gst)
        data.save()
        return render(request, 'datatables.html')

    else:
        return redirect('/')

def remove_customer(request, customer_id):
    if request.method == "POST":
        customer_id = request.POST['id']
        customer = Customer.objects.get(pk= customer_id)
        customer_delete = Customer.objects.delete(customer)
        customer_delete.save()
        return redirect('datatables/')
    else:
        return redirect('datatables/')