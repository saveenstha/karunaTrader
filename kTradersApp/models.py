from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Common model for tracking created info
class TimeStampedModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

# Product types, e.g., red, white, blue potatoes
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Buyers (clients across the country)
class Buyer(TimeStampedModel):
    company_name = models.CharField(max_length=255)
    pan_num = models.CharField(
        max_length=9,
        primary_key=True,
        validators=[RegexValidator(r'^\d{1,9}$')]
    )
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.company_name

# Owner Details (of Buyer company)
class OwnerDetails(models.Model):
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Farmers (suppliers)
class Farmer(TimeStampedModel):
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Purchases from farmers
class Purchase(TimeStampedModel):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)

    def total_cost(self):
        return self.quantity_kg * self.price_per_kg

# Sales to buyers
class Sale(TimeStampedModel):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    transport_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    billing_info = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def total_amount(self):
        return (self.quantity_kg * self.price_per_kg) + self.transport_charge
