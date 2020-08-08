from django.db import models
from django.db.models.signals import post_save
from num2words import num2words


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    city = models.CharField(max_length=12)
    state = models.CharField(max_length=15)
    gst_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    slug = models.SlugField()
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=500,null=True)
    invoice_no = models.CharField(max_length=500,null=True)
    hsn_code = models.CharField(max_length=4)
    dated = models.DateField()
    transport = models.CharField(max_length=500,null=True)
    vehicle_no = models.CharField(max_length=500,null=True)
    challan_no = models.CharField(max_length=500,null=True)
    date =  models.DateField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
