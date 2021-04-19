from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.
class Buyer(models.Model):
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    mobile = models.BigIntegerField()
    pan_num = models.CharField(max_length=9, primary_key=True, validators=[RegexValidator(r'^\d{1,10}$')])
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('buyer-list')

class Transaction(models.Model):
    txn_date = models.DateField(default=timezone.now)
    bill_number = models.IntegerField(unique=True)
    pan_num = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    total_amount = models.IntegerField()
    transport_vehicle = models.CharField(max_length=15)
    driver_contact = models.BigIntegerField()
    vehicle_fare = models.IntegerField()
    total_package = models.IntegerField(default=0)
    fare_per_package_rate = models.SmallIntegerField(default=0)
    labour_cost = models.IntegerField(default=0)


    def __str__(self):
        return "bill-no : " + str(self.bill_number)

    def get_absolute_url(self):
        return reverse('buyer-list')


class ParticularsDetail(models.Model):
    bill_number = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    particulars = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.SmallIntegerField()
    goods_amount = models.IntegerField()

    def __str__(self):
        return "BN: "+str(self.bill_number)+self.particulars