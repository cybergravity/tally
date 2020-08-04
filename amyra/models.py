from django.db import models
from django.db.models.signals import post_save
from num2words import num2words


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=60)
    city = models.CharField(max_length=12)
    state = models.CharField(max_length=15)
    gst_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
