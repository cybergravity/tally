from django.db import models

# Create your models here.
class Customer(models.Model):
    title = models.CharField(max_length=255)
    name= models.CharField(max_length=50)
    address = models.TextField()
    mobile_no = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name