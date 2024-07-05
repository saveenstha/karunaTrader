from django.db import models
from django.utils import timezone
from django.urls import reverse
from kTradersApp.models import Buyer


# # Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    bill_number = models.IntegerField(unique=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(default=timezone.now)

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
