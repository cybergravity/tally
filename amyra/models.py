import datetime

from django.db import models
from django.db.models.signals import post_save
from num2words import num2words
from django.utils.translation import ugettext_lazy as _


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

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Destination(models.Model):
    slug = models.SlugField(null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=500, null=True)
    invoice_no = models.CharField(max_length=500, null=True)
    hsn_code = models.CharField(max_length=4)
    dated = models.DateField()
    transport = models.CharField(max_length=500, null=True)
    vehicle_no = models.CharField(max_length=500, null=True)
    challan_no = models.CharField(max_length=500, null=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    transport_cost = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


class Calculation(models.Model):
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
    total_amount = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    igst = models.IntegerField(null=True, blank=True)
    total_amount_after_tax = models.IntegerField(null=True, blank=True)
    total_amount_in_words = models.CharField(max_length=500, null=True, blank=True, default='')


DIBBI_CHOICE = (
    (6, '6 dibbi'),
    (12, '12 dibbi')
)


class Item(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    sr_no = models.IntegerField()
    design_name = models.CharField(max_length=500)
    qty = models.IntegerField()
    dibbi = models.IntegerField(choices=DIBBI_CHOICE, default=12)
    pics = models.IntegerField(null=True, blank=True, editable=False)
    rate = models.IntegerField()
    amount = models.IntegerField(null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.sr_no)


def calculate_bill(sender, instance, created, **kwargs):
    if created:
        post_save.connect(calculate_bill, sender=Destination)
    else:
        items = Item.objects.filter(destination=instance)

        total = 0
        for item in items:
            pics = item.qty * item.dibbi
            amount = pics * item.rate
            item.amount = amount
            item.pics = pics
            item.save()
            total += amount
        total_amount = total
        sgst = int(total_amount * 1.5 / 100)
        cgst = int(total_amount * 1.5 / 100)
        total_amount_after_tax = total_amount + sgst + cgst
        total_amount_in_words = (num2words(total_amount_after_tax, lang='en_IN') + ' Rupees Only')
        try:
            calculation = Calculation.objects.get(destination=instance)
            calculation.pics = pics
            calculation.total_amount = total_amount
            calculation.sgst = sgst
            calculation.cgst = cgst
            calculation.total_amount_after_tax = total_amount_after_tax
            calculation.total_amount_in_words = total_amount_in_words
        except:
            calculation = Calculation.objects.create(destination=instance, total_amount=total_amount, sgst=sgst,
                                                     cgst=cgst, total_amount_after_tax=total_amount_after_tax,
                                                     total_amount_in_words=total_amount_in_words)
        calculation.save()


post_save.connect(calculate_bill, sender=Destination)


def file_location_path(instance, filename):
    result = []
    a = instance.folder
    while True:
        if a is None:
            break
        else:
            result.insert(0, str(a))
            a = a.parent
    result = '/'.join(result)
    return f'drive/{result}/{filename}'


class Folder(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='folders', null=True, blank=True)
    name = models.CharField(_('Folder Name'), max_length=70)

    def __str__(self):
        return self.name


class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='folderfiles')
    file = models.FileField(_('File'), upload_to=file_location_path, null=True, blank=True)
