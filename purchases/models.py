from django.db import models
from people.models import Farmer
from inventory.models import Product

# -- Purchase Models --
# Purchases from farmers

class PurchaseBill(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    purchase_bill_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Purchase - {self.farmer.name} [{self.date}]"


class PurchaseItem(models.Model):
    purchase_bill_number = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sacks = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=7, decimal_places=2)  # actual weight
    rate_per_kg = models.DecimalField(max_digits=6, decimal_places=2)

    def total_price(self):
        return self.weight_kg * self.rate_per_kg