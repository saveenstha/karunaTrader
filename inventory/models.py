from django.db import models


# Product types, e.g., red, white, blue potatoes
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class DailyRate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    purchase_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    sales_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        unique_together = ('product', 'date')

    def __str__(self):
        return f"{self.product.name} on {self.date}"