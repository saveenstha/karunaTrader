from django.db import models
from mainapp.models import TimeStampedModel
from people.models import Buyer
from inventory.models import Product

# # Sales to buyers
# class Sale(TimeStampedModel):
#     buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
#     price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
#     transport_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     billing_info = models.TextField(blank=True, null=True)
#     date = models.DateField(default=timezone.now)
#
#     def total_amount(self):
#         return (self.quantity_kg * self.price_per_kg) + self.transport_charge


# -- Sales Models --

class SalesBill(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    date = models.DateField()
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    transportation_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    sales_bill_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Sale - {self.buyer.company_name} [{self.date}]"


class SalesItem(models.Model):
    sales_bill_number = models.ForeignKey(SalesBill, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sacks = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=7, decimal_places=2)
    rate_per_kg = models.DecimalField(max_digits=6, decimal_places=2)

    def total_price(self):
        return self.weight_kg * self.rate_per_kg