from django.db import models
from django.utils import timezone
from django.urls import reverse
from kTradersApp.models import Buyer


# # Create your models here.
class Transactions(models.Model):
    txn_date = models.DateField(default=timezone.now, null=True)
    pan_num = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    bill_number = models.IntegerField(unique=True)
    credit_amount = models.IntegerField(null=True)
    debit_amount = models.IntegerField(null=True)
    balance_after_transaction = models.IntegerField(default=0)

    def __str__(self):
        return "bill-no : " + str(self.bill_number)

    def get_absolute_url(self):
        return reverse('buyer-list')



# class ParticularsDetail(models.Model):
#     txn_id = models.DateField(default=timezone.now)
#     txn_date = models.DateField(default=timezone.now)
#     document_id = models.ForeignKey(Transaction, on_delete= models.RESTRICT)
#     particulars = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     rate = models.SmallIntegerField()
#     goods_amount = models.IntegerField()
#     transport_vehicle = models.CharField(max_length=15, default=0)
#     driver_contact = models.CharField(max_length=10, default=0)
#     vehicle_fare = models.IntegerField(default=0)
#     total_package = models.IntegerField(default=0)
#     fare_per_package_rate = models.SmallIntegerField(default=0)
#     labour_cost = models.IntegerField(default=0)
#     total_amount = models.IntegerField(default=0)
#
#     def __str__(self):
#         return str(self.document_id)
#
#
